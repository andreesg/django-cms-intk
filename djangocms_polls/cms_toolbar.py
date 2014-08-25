# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar

from .models import Poll

#@toolbar_pool.register
#class PollsToolbar(CMSToolbar):
#	def populate(self):
#		menu = self.toolbar.get_or_create_menu('poll-app', _('Polls'))
#		url = reverse('admin:polls_poll_changelist')
#		menu.add_modal_item(_('Poll overview'), url=url)
