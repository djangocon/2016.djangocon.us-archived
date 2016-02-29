from django import forms
from markitup.widgets import MarkItUpWidget

from .models import OpenSpaceProposal, TalkProposal, TutorialProposal


class ProposalForm(forms.ModelForm):

    def clean_description(self):
        value = self.cleaned_data["description"]
        if len(value) > 400:
            raise forms.ValidationError(
                u"The description must be less than 400 characters"
            )
        return value


class OpenSpaceProposalForm(ProposalForm):

    class Meta:
        model = OpenSpaceProposal
        fields = [
            "title",
            "description",
            "abstract",
            "additional_notes",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
        }


class TalkProposalForm(ProposalForm):

    class Meta:
        model = TalkProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "special_requirements",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
            "special_requirements": MarkItUpWidget(),
        }


class TutorialProposalForm(ProposalForm):

    class Meta:
        model = TutorialProposal
        fields = [
            "title",
            "audience_level",
            "description",
            "abstract",
            "additional_notes",
            "special_requirements",
            "recording_release",
        ]
        widgets = {
            "abstract": MarkItUpWidget(),
            "additional_notes": MarkItUpWidget(),
            "special_requirements": MarkItUpWidget(),
        }
