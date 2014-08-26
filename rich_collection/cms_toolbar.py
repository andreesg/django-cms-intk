# -*- coding: utf-8 -*-

from cms.api import get_page_draft
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar
from cms.utils import get_cms_setting
from cms.utils.permissions import has_page_change_permission
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext_lazy as _
from cms.utils.urlutils import add_url_parameters
from cms.utils.permissions import get_user_sites_queryset, has_page_change_permission

@toolbar_pool.register
class RichCollectionToolbar(CMSToolbar):
    def populate(self):
        # always use draft if we have a page
        self.page = get_page_draft(self.request.current_page)

        if self.page and has_page_change_permission(self.request):
            return