from django.contrib import admin

from . import models


class ProposalAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'speaker',
        'speaker_email',
        'kind',
        'audience_level',
        'cancelled',
    ]

    list_filter = [
        'kind__name',
        'result__accepted',
    ]

    raw_id_admin = [
        'speaker',
    ]


@admin.register(models.TalkProposal)
class TalkProposalAdmin(ProposalAdmin):
    pass


@admin.register(models.TutorialProposal)
class TutorialProposalAdmin(ProposalAdmin):
    pass
