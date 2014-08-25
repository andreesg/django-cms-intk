# -*- coding: utf-8 -*-
# from django.core.urlresolvers import reverse
# from django.utils.translation import ugettext_lazy as _

# from cms.toolbar_pool import toolbar_pool
# from cms.toolbar_base import CMSToolbar

#from .models import RichPage

# @toolbar_pool.register
# class RichPageToolbar(CMSToolbar):
# 	def populate(self):
# 		menu = self.toolbar.get_or_create_menu("rich-page", _("Rich Page"))
# 		url = reverse('admin:rich_page_richpage_add')
# 		menu.add_modal_item(_('Add Rich Page'), url=url)

from cms.api import get_page_draft
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils import get_cms_setting
from cms.utils.permissions import has_page_change_permission
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from .models import RichPage


@toolbar_pool.register
class RichPageToolbar(CMSToolbar):
    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if not self.page:
            # Nothing to do
            return

        # check global permissions if CMS_PERMISSIONS is active
        if get_cms_setting('PERMISSION'):
            has_global_current_page_change_permission = has_page_change_permission(self.request)
        else:
            has_global_current_page_change_permission = False
            # check if user has page edit permission
        can_change = self.request.current_page and self.request.current_page.has_change_permission(self.request)
        if has_global_current_page_change_permission or can_change:
            try:
                rich_page = RichPage.objects.get(extended_object_id=self.page.id)
            except RichPage.DoesNotExist:
                rich_page = None
            try:
                if rich_page:
                    url = reverse('admin:rich_page_richpage_change', args=(rich_page.pk,))
                else:
                    url = reverse('admin:rich_page_richpage_add') + '?extended_object=%s' % self.page.pk
            except NoReverseMatch:
                # not in urls
                pass
            else:
                not_edit_mode = not self.toolbar.edit_mode
                menu = self.toolbar.get_or_create_menu('rich-page-new', _('Rich Page Content'))
                if rich_page:
                	menu.add_modal_item(_('Edit content'), url=url)
                else:
                	menu.add_modal_item(_('Add content'), url=url)

