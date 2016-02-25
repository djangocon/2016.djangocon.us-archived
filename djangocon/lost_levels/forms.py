from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.forms.models import inlineformset_factory, BaseInlineFormSet
from django.forms.widgets import RadioSelect
from symposion.sponsorship.models import Sponsor, SponsorBenefit, SponsorLevel


class SponsorApplicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        self.choices = kwargs.pop("choices")
        kwargs.update({
            "initial": {
                "contact_name": self.user.get_full_name,
                "contact_email": self.user.email
            }
        })
        super(SponsorApplicationForm, self).__init__(*args, **kwargs)
        # self.fields["invoice_name"].required = False
        # self.fields["invoice_email"].required = False
        # self.fields["graphics_name"].required = False
        # self.fields["graphics_email"].required = False
        self.fields['level'] = forms.ChoiceField(
            choices=self.choices,
            label="Benefit level options",
            widget=RadioSelect
        )
        if not self.user.is_staff:
            del self.fields["active"]

    class Meta:
        model = Sponsor
        fields = [
            "name",
            "external_url",
            "contact_name",
            "contact_email",
            # "invoice_name",
            # "invoice_email",
            # "graphics_name",
            # "graphics_email",
            "level",
            "active"
        ]

    def clean(self):
        level = SponsorLevel.objects.get(name=self.cleaned_data['level'])
        print type(level)
        self.cleaned_data['level'] = level
        return self.cleaned_data

    def save(self, commit=True):
        obj = super(SponsorApplicationForm, self).save(commit=False)
        obj.applicant = self.user
        if commit:
            obj.save()
        return obj


class SponsorDetailsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(SponsorDetailsForm, self).__init__(*args, **kwargs)
        # self.fields["invoice_name"].required = False
        # self.fields["invoice_email"].required = False
        # self.fields["graphics_name"].required = False
        # self.fields["graphics_email"].required = False
        if not self.user.is_staff:
            del self.fields["active"]

    class Meta:
        model = Sponsor
        fields = [
            "name",
            "external_url",
            "contact_name",
            "contact_email",
            # "invoice_name",
            # "invoice_email",
            # "graphics_name",
            # "graphics_email",
            "active"
        ]


class SponsorBenefitsInlineFormSet(BaseInlineFormSet):

    def _construct_form(self, i, **kwargs):
        form = super(SponsorBenefitsInlineFormSet, self)._construct_form(
            i, **kwargs)

        # only include the relevant data fields for this benefit type
        fields = form.instance.data_fields()
        form.fields = dict(
            (k, v) for (k, v) in form.fields.items() if k in fields + ["id"])

        for field in fields:
            # don't need a label, the form template will label it with the
            # benefit name
            form.fields[field].label = ""

            # provide word limit as help_text
            if form.instance.benefit.type == "text" and form.instance.max_words:
                form.fields[
                    field].help_text = u"maximum %s words" % form.instance.max_words

            # use admin file widget that shows currently uploaded file
            if field == "upload":
                form.fields[field].widget = AdminFileWidget()

        return form


SponsorBenefitsFormSet = inlineformset_factory(
    Sponsor, SponsorBenefit,
    formset=SponsorBenefitsInlineFormSet,
    can_delete=False, extra=0,
    fields=["text", "upload"]
)


class SponsorPassesForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.tickets = kwargs.pop("tickets")
        self.sponsors = kwargs.pop("sponsors")
        super(SponsorPassesForm, self).__init__(*args, **kwargs)
        self.fields["ticket_names"] = forms.MultipleChoiceField(
            choices=self.tickets)
        self.fields["sponsor"] = forms.ChoiceField(choices=self.sponsors)

    number_of_passes = forms.IntegerField()
    amount_off = forms.FloatField(required=False)
    percent_off = forms.IntegerField(max_value=100, required=False)

    def clean(self):
        amount_off = self.cleaned_data['amount_off']
        percent_off = self.cleaned_data['percent_off']

        if amount_off and percent_off:
            raise forms.ValidationError(
                'Please enter in either amount OR percent off')
        elif amount_off is None and percent_off is None:
            raise forms.ValidationError(
                'Please provide either an amount OR percent off')

        return self.cleaned_data
