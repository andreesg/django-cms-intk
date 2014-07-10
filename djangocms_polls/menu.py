# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import Poll

class PollsMenu(CMSAttachMenu):
	name = _("Polls Menu") # give the menu a name, this is required.
	def get_nodes(self, request):
		nodes = []
		for poll in Poll.objects.all():
			node = NavigationNode(poll.question, reverse('polls:detail', args=(poll.pk,)),poll.pk)
			nodes.append(node)
		return nodes

menu_pool.register_menu(PollsMenu)


