from django.shortcuts import render
from symposion.schedule.models import Slot
from django.contrib.sites.models import Site

from django.core.urlresolvers import reverse
from django.http import HttpResponse
import json
from django.template.loader import render_to_string
from pinax.blog.models import Post
from datetime import datetime


def json_serializer(obj):
    if isinstance(obj, datetime.time):
        return obj.strftime("%H:%M")
    raise TypeError


def duration(start, end):
    start_dt = datetime.strptime(start.isoformat(), "%H:%M:%S")
    end_dt = datetime.strptime(end.isoformat(), "%H:%M:%S")
    delta = end_dt - start_dt
    return delta.seconds // 60


def homepage(request):
    return render(request, "homepage.html", {
        'latestposts': Post.objects.published().order_by("published")[:10]})


def schedule_json(request):
    slots = Slot.objects.all().order_by("start")
    data = []
    slot_data = {}
    for slot in slots:
        if slot.kind.label in ["talk", "tutorial", "plenary"] and slot.content and slot.content.proposal.kind.slug in [
            "talk", "tutorial"]:
            if hasattr(slot.content.proposal, "recording_release"):
                slot_data = {
                    "name": slot.content.title,
                    "room": ", ".join(room["name"] for room in slot.rooms.values()),
                    "start": datetime.combine(slot.day.date, slot.start).isoformat(),
                    "end": datetime.combine(slot.day.date, slot.end).isoformat(),
                    "duration": duration(slot.start, slot.end),
                    "authors": [s.name for s in slot.content.speakers()],
                    "released": slot.content.proposal.recording_release,
                    "license": "",
                    "contact": [s.email for s in slot.content.speakers()] if request.user.is_staff else [
                        "redacted"],
                    "abstract": slot.content.abstract.raw,
                    "description": slot.content.description.raw,
                    "conf_key": slot.pk,
                    "conf_url": "https://%s%s" % (
                        Site.objects.get_current().domain,
                        reverse("schedule_presentation_detail", args=[slot.content.pk])
                    ),

                    "kind": slot.content.proposal.kind.slug,
                    "tags": "",
                }
        elif slot.kind.label == "lightning":
            slot_data = {
                "name": slot.content_override.raw if slot.content_override else "Lightning Talks",
                "room": ", ".join(room["name"] for room in slot.rooms.values()),
                "start": datetime.combine(slot.day.date, slot.start).isoformat(),
                "end": datetime.combine(slot.day.date, slot.end).isoformat(),
                "duration": duration(slot.start, slot.end),
                "authors": None,
                "released": True,
                "license": "",
                "contact": None,
                "abstract": "Lightning Talks",
                "description": "Lightning Talks",
                "conf_key": slot.pk,
                "conf_url": None,
                "kind": slot.kind.label,
                "tags": "",
            }
        else:
            continue
        data.append(slot_data)

    return HttpResponse(
        json.dumps(data, default=json_serializer),
        content_type="application/json"
    )


def guidebook_news_feed(request):
    """
    Sections are broken in the version of `biblion` that we are using so
    lifting this form `pinax-blog` which is the successor.

    https://github.com/pinax/pinax-blog/blob/master/pinax/blog/views.py#L146
    """
    current_site = Site.objects.get_current()

    feed_title = 'DjangoCon US News Updates'
    feed_description = 'The latest updates and additions for DjangoCon US.'
    feed_mimetype = 'application/rss+xml'
    feed_template = 'pinax/blog/rss_feed.xml'

    blog_url = 'http://%s%s' % (current_site.domain, reverse('blog'))
    # feed_url = 'http://%s%s' % (current_site.domain, reverse(url_name, kwargs=kwargs))

    posts = Post.objects.published().exclude(title__endswith='Sponsor') \
        .order_by('-published')

    if posts:
        feed_updated = posts[0].updated
    else:
        feed_updated = datetime(2009, 8, 1, 0, 0, 0)

    feed = render_to_string(feed_template, {
        # 'feed_id': feed_url,
        'feed_title': feed_title,
        'feed_description': feed_description,
        'blog_url': blog_url,
        # 'feed_url': feed_url,
        'feed_updated': feed_updated,
        'entries': posts,
        'current_site': current_site,
    })

    return HttpResponse(feed, content_type=feed_mimetype)
