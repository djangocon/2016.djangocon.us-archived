# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('symposion_proposals', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalkProposal',
            fields=[
                ('proposalbase_ptr', models.OneToOneField(primary_key=True, to='symposion_proposals.ProposalBase', parent_link=True, auto_created=True, serialize=False)),
                ('audience_level', models.IntegerField(choices=[(1, b'Novice'), (3, b'Intermediate'), (2, b'Experienced')])),
                ('recording_release', models.BooleanField(help_text=b'By submitting your proposal, you agree to give permission to the conference organizers to record, edit, and release audio and/or video of your presentation. If you do not agree to this, please uncheck this box.', default=True)),
            ],
            options={
                'verbose_name': 'talk proposal',
            },
            bases=('symposion_proposals.proposalbase',),
        ),
    ]
