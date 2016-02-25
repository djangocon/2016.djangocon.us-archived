"""
These views are part of the "Lost Levels" of previous DjangoCons and
various forks of Symposion.

In theory, we could be using them but we are not.

ref: https://github.com/djangocon/symposion/blob/master/symposion/views.py

"""

import eventbrite
import json
import os
import StringIO

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from symposion.sponsorship.models import Sponsor
from symposion.utils.mail import send_email
from zipfile import ZipFile, ZIP_DEFLATED

from .forms import SponsorPassesForm


@login_required
def eventbrite_confirm(request):
    user = request.user
    for spsr in Sponsor.objects.filter(active=True):
        if user.email in spsr.sponsor_contacts:
            sponsor = spsr
            if not request.GET['oid'] == '':
                    sponsor.paid = True
                    sponsor.save()
            return redirect("sponsor_detail", pk=sponsor.pk)
        elif user.is_staff:
            messages.warning(request, "Remember to set paid to 'True' in admin for this sponsor.")
            return redirect("dashboard")


@login_required
def sponsor_passes(request):
    if not request.user.is_staff:
        raise Http404()

    # Turn back if eventbrite not being used or if config data missing from settings
    if not settings.EVENTBRITE:
        messages.error(request, "We're sorry, Eventbrite isn't being used for this conference.")
        return redirect('dashboard')
    elif settings.EB_APP_KEY == '' or settings.EB_USER_KEY == '' or settings.EB_EVENT_ID == '':
        messages.error(request, "Eventbrite client has not been configured properly in settings. Please contact conference organizer about this issue.")
        return redirect('dashboard')
    else:
        # grab authentication credentials
        eb_event_id = settings.EB_EVENT_ID
        eb_auth_tokens = {
            'app_key': settings.EB_APP_KEY,
            'user_key': settings.EB_USER_KEY
        }

        # Make first request for basic event and ticket info
        eb_client = eventbrite.EventbriteClient(eb_auth_tokens)
        response = eb_client.event_get({
            'id': eb_event_id
        })

        # Make choices list of ticket names and prices for our form
        TICKET_CHOICES = []
        ticket_dict = {}
        tickets = response['event']['tickets']
        for tkt in tickets:
            ticket = tkt['ticket']
            # don't include donation ('type' == 1) tickets
            if ticket['type'] != 1:
                ticket_name = ticket['name']
                ticket_id = ticket['id']
                price = ticket['price']

            # Make dict of name/id pairs for discount generation
                ticket_dict[ticket_name] = ticket_id

            # Make our choices list for form
                TICKET_CHOICES.append((ticket_name, ticket_name + ' -- $' + price))

        # Next, make a list of *active* sponsors to add to our form
        SPONSOR_CHOICES = []
        for sponsor in Sponsor.objects.filter(active=True):
            SPONSOR_CHOICES.append((sponsor, sponsor))

        # we also need event title and url for our email
        event_title = response['event']['title']
        event_url = response['event']['url']

        # If form is valid, process form and generate discount
        if request.method == "POST":
            form = SponsorPassesForm(request.POST, tickets=TICKET_CHOICES, sponsors=SPONSOR_CHOICES)

            if form.is_valid():
                sponsor = form.cleaned_data["sponsor"]
                ticket_names = form.cleaned_data["ticket_names"]
                amount_off = form.cleaned_data["amount_off"]
                percent_off = form.cleaned_data["percent_off"]

                # match selected ticket types to ticket ids from our dict
                tickets_list = ','.join(str(v) for k, v in ticket_dict.iteritems() if k in ticket_names)

                # Eventbrite will only accept one of the following: amount_off or percent_off
                # Create variables to pass into our request one or other depending on staff input
                if amount_off is not None and percent_off is None:
                    discount_n = 'amount_off'
                    discount_v = amount_off
                elif percent_off is not None and amount_off is None:
                    discount_n = 'percent_off'
                    discount_v = percent_off

                # Generate discount code
                discount_code = (sponsor[:6] + '_' + event_title[:6]).replace(' ', '')

                # Alert user if discount already exists
                # Except case where no discounts exist to check against
                try:
                    response = eb_client.event_list_discounts({
                        'id': eb_event_id
                    })
                    for dsct in response['discounts']:
                        discount = dsct['discount']
                        if discount['code'] == discount_code:
                            messages.error(request, "Oops, looks like that discount code already exists")
                            return redirect("sponsor_passes")

                except EnvironmentError:
                    response = ''
                    pass

                # Send request to eventbrite to register the discount code w/params
                response = eb_client.discount_new({
                    'event_id': eb_event_id,
                    'code': discount_code,
                    discount_n: discount_v,
                    'quantity_available': int(form.cleaned_data["number_of_passes"]),
                    'tickets': tickets_list
                })

                # Auto-email to sponsor contact with discount code
                for spsr in Sponsor.objects.filter(name=sponsor):
                    contact_name = spsr.contact_name
                    contact_email = spsr.contact_email

                event_email = settings.EVENT_EMAIL
                event_phone = settings.EVENT_PHONE

                message_ctx = {
                    "event_name": event_title,
                    "sponsor": sponsor,
                    "contact_name": contact_name,
                    "discount_code": discount_code,
                    "event_url": event_url,
                    "event_contact_email": event_email,
                    "event_contact_phone": event_phone
                }
                send_email(
                    [contact_email], "sponsor_passes",
                    context=message_ctx
                )

                messages.success(request, "Discount code was generated and has been emailed to sponsor contact")

                return redirect("dashboard")
        else:
            form = SponsorPassesForm(sponsors=SPONSOR_CHOICES, tickets=TICKET_CHOICES)

        return render_to_response("sponsorship/passes.html", {
            "form": form,
        }, context_instance=RequestContext(request))


# with print logos and json reformat
@login_required
def export_sponsors(request):
    if not request.user.is_staff:
        raise Http404()

    # use StringIO to make zip in memory, rather than on disk
    f = StringIO.StringIO()
    z = ZipFile(f, 'w', ZIP_DEFLATED)
    data = []

    # collect the data and write web and print logo assets for each sponsor
    for sponsor in Sponsor.objects.all():
        data.append({
            'name': sponsor.name,
            'website': sponsor.external_url,
            'description': sponsor.listing_text,
            'contact name': sponsor.contact_name,
            'contact email': sponsor.contact_email,
            'level': str(sponsor.level),
        })
        if sponsor.website_logo:
            path = sponsor.website_logo.path
            z.write(path, '{0}_weblogo{1}'.format(
                str(sponsor.name).replace(' ', ''),
                os.path.splitext(path)[1]))
        if sponsor.print_logo:
            path = sponsor.print_logo.path
            z.write(path, '{0}_printlogo{1}'.format(
                str(sponsor.name).replace(' ', ''),
                os.path.splitext(path)[1]))

    # write sponsor data to text file for zip
    with open('sponsor_data.txt', 'wb') as d:
        json.dump(data, d, encoding='utf-8', indent=4)
    z.write('sponsor_data.txt')

    z.close()

    response = HttpResponse(mimetype='application/zip')
    response['Content-Disposition'] = 'attachment; filename=sponsor_file.zip'
    f.seek(0)
    response.write(f.getvalue())
    f.close()
    return response
