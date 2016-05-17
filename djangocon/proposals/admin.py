from django.contrib import admin

from . import models


def mark_proposal_as_accepted(modeladmin, request, queryset):
    for proposal in queryset:
        # proposal.result.accepted = True
        proposal.result.status = 'accepted'
        proposal.result.save()
mark_proposal_as_accepted.short_description = "Mark selected proposal status as accepted"


def mark_proposal_as_rejected(modeladmin, request, queryset):
    for proposal in queryset:
        # proposal.result.accepted = False
        proposal.result.status = 'rejected'
        proposal.result.save()
mark_proposal_as_rejected.short_description = "Mark selected proposal status as rejected"


def mark_proposal_as_standby(modeladmin, request, queryset):
    for proposal in queryset:
        # proposal.result.accepted = None
        proposal.result.status = 'standby'
        proposal.result.save()
mark_proposal_as_standby.short_description = "Mark selected proposal status as standby"


def mark_proposal_as_undecided(modeladmin, request, queryset):
    for proposal in queryset:
        # proposal.result.accepted = None
        proposal.result.status = 'undecided'
        proposal.result.save()
mark_proposal_as_undecided.short_description = "Mark selected proposal status as undecided"


class ProposalAdmin(admin.ModelAdmin):
    actions = [
        mark_proposal_as_accepted,
        mark_proposal_as_rejected,
        mark_proposal_as_standby,
        mark_proposal_as_undecided,
    ]

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
        'result__status',
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
