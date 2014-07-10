# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool

from .models import RichPage

# class RichPageMenu(CMSAttachMenu):
# 	name = _("Rich Page Menu")

# 	def get_nodes(self, request):
# 		nodes = []
# 		for page in RichPage.objects.all():
# 			node = NavigationNode(page.title, reverse('rich_page:detail', args=(page.slug,)), page.slug)
# 			nodes.append(node)
# 		return nodes

# menu_pool.register_menu(RichPageMenu)
