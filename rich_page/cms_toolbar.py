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
from .models import RichPage, RichSlideshow
from rich_collection.models import RichCollection
from cms.utils.urlutils import add_url_parameters
from cms.utils.permissions import get_user_sites_queryset, has_page_change_permission


PAGE_MENU_BREAK = 'Page Menu Break'
PAGE_MENU_ADD = 'admin:cms_page_add'
RICHPAGE_MENU_ADD = 'admin:rich_page_richpage_add'
RICHSLIDESHOW_MENU_ADD = 'admin:rich_page_richslideshow_add'
RICHSLIDESHOW_MENU_CHANGE = 'admin:rich_page_richslideshow_change'
RICHPAGE_MENU_CHANGE = 'admin:rich_page_richpage_change'
RICHCOLLECTION_MENU_ADD = 'admin:rich_collection_richcollection_add'
RICHCOLLECTION_MENU_CHANGE = 'admin:rich_collection_richcollection_change'

@toolbar_pool.register
class RichPageToolbar(CMSToolbar):
    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if self.page and has_page_change_permission(self.request):
            page_url = reverse(PAGE_MENU_ADD)
            rich_page_add_url = reverse(RICHPAGE_MENU_ADD) + '?extended_object=%s' % self.page.pk
            rich_collection_add_url = reverse(RICHCOLLECTION_MENU_ADD) + '?extended_object=%s' % self.page.pk
            rich_slideshow_add_url = reverse(RICHSLIDESHOW_MENU_ADD) + '?extended_object=%s' % self.page.pk

            sub_page_params = {'edit': 1, 'position': 'last-child', 'target': self.page.pk}

            menu = self.toolbar.get_or_create_menu('rich-page-new', _('Create Page'))
            menu.add_modal_item(_('Create Page'), url=page_url)
            menu.add_modal_item(_('Create Sub Page'), url=add_url_parameters(page_url, sub_page_params))

            try:
                rich_page = RichPage.objects.get(extended_object_id=self.page.id)
            except RichPage.DoesNotExist:
                rich_page = None

            try:
                rich_collection = RichCollection.objects.get(extended_object_id=self.page.id)
            except RichCollection.DoesNotExist:
                rich_collection = None

            try:
                rich_slideshow = RichSlideshow.objects.get(extended_object_id=self.page.id)
            except RichSlideshow.DoesNotExist:
                rich_slideshow = None

            if not rich_page and not rich_collection:
                menu.add_break(PAGE_MENU_BREAK)
                menu.add_modal_item(_('Add Article'), url=rich_page_add_url)
                menu.add_modal_item(_('Add Collection'), url=rich_collection_add_url)

            if rich_page:
                menu.add_break(PAGE_MENU_BREAK)
                if rich_slideshow:
                    rich_slideshow_change_url = reverse(RICHSLIDESHOW_MENU_CHANGE, args=(rich_slideshow.pk,)) + '?extended_object=%s' % self.page.pk
                    menu.add_modal_item(_('Remove Slideshow'), url=rich_slideshow_change_url)
                else:
                    menu.add_modal_item(_('Add Slideshow'), url=rich_slideshow_add_url)
                rich_page_change_url = reverse(RICHPAGE_MENU_CHANGE, args=(rich_page.pk,)) + '?extended_object=%s' % self.page.pk
                menu.add_modal_item(_('Remove Article'), url=rich_page_change_url)

            elif rich_collection:
                menu.add_break(PAGE_MENU_BREAK)
                rich_collection_change_url = reverse(RICHCOLLECTION_MENU_CHANGE, args=(rich_collection.pk,)) + '?extended_object=%s' % self.page.pk
                menu.add_modal_item(_('Remove Collection'), url=rich_collection_change_url)

