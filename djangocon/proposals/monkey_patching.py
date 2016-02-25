# This is horrible and we shouldn't do it, but changing
# symposium is probably outside of our wheelhouse right now

from symposion.proposals.models import ProposalBase

def __unicode__(self):
	return self.title

ProposalBase.add_to_class('__unicode__', __unicode__)