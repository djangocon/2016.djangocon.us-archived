from django.db import models
from django.utils.translation import ugettext_lazy as _
from markitup.fields import MarkupField
from symposion.proposals.models import ProposalBase


class Proposal(ProposalBase):

    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3
    AUDIENCE_LEVEL_NOT_APPLICABLE = 4

    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, "Novice"),
        (AUDIENCE_LEVEL_INTERMEDIATE, "Intermediate or Advanced"),
        # (AUDIENCE_LEVEL_EXPERIENCED, "Experienced"),
        (AUDIENCE_LEVEL_NOT_APPLICABLE, "Not Applicable"),
    ]

    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    recording_release = models.BooleanField(
        default=True,
        help_text=_("By submitting your talk proposal, you agree to give "
                    "permission to the conference organizers to record, edit, "
                    "and release audio and/or video of your presentation. If "
                    "you do not agree to this, please uncheck this box."),
    )

    special_requirements = MarkupField(
        _("Special Requirements"),
        blank=True,
        help_text=_("If you have any special requirements such as needing "
                    "travel assistance, accessibility needs, or anything "
                    "else please let us know here so that  we may plan "
                    "accordingly. (This is not made public nor will the "
                    "review committee have access to view it.)")
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"%s" % self.title


class TalkProposal(Proposal):
    pass


class TutorialProposal(Proposal):
    pass


class OpenSpaceProposal(ProposalBase):
    pass
