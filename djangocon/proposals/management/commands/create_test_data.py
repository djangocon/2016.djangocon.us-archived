from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.core.urlresolvers import reverse
from faker import Factory

from djangocon.proposals import models
from symposion.proposals import models as symposion_proposal_models
from symposion.speakers.models import Speaker


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Factory.create()
        proposal_kind, _ = symposion_proposal_models.ProposalKind.objects.get_or_create(
            name='25 minute talk',
            slug='talk-25-min',
        )
        user_bob, _ = User.objects.get_or_create(username='bob-the-builder')
        speaker_bob, _ = Speaker.objects.update_or_create(
            user=user_bob,
            defaults={
                'biography': 'Can Bob build it in Django? Yes, he can!'
            }
        )
        talk_proposal, _ = models.TalkProposal.objects.update_or_create(
            speaker=speaker_bob,
            title='How to write a test proposal in Django',
            kind=proposal_kind,
            audience_level=models.Proposal.AUDIENCE_LEVEL_NOVICE,
            defaults={
                'description': fake.text(),
                'abstract': fake.text(),
                'additional_notes': fake.text(),
                'recording_release': fake.text(),
                'special_requirements': fake.text(),
            }
        )

        print('speaker detail page: {0}'.format(reverse('speaker_profile', args=[speaker_bob.pk])))
        print('proposal detail page: {0}'.format(reverse('proposal_detail', args=[talk_proposal.pk])))
