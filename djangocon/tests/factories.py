import factory

from djangocon.proposals import models as proposals


class ProposalFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = proposals.Proposal

    audience_level = factory.fuzzy.FuzzyChoice([
        proposals.Proposal.AUDIENCE_LEVEL_NOVICE,
        proposals.Proposal.AUDIENCE_LEVEL_EXPERIENCED,
        proposals.Proposal.AUDIENCE_LEVEL_INTERMEDIATE,
    ])
    recording_release = factory.fuzzy.FuzzyChoice([True, False])


class TalkProposalFactory(ProposalFactory):
    pass


class TutorialProposalFactory(ProposalFactory):
    pass


class OpenSpaceProposalFactory(ProposalFactory):
    pass
