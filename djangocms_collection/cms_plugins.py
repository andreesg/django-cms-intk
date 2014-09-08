# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from cms.utils import get_language_from_request
from .models import Collection
from .utils import get_subpage_content_from_page

class CollectionPlugin(CMSPluginBase):
    model = Collection
    name = _("Collection")
    module = _("Collection")
    render_template = "djangocms_collection/base.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        request = context["request"]
        language = get_language_from_request(request)
        page = request.current_page
        list_plugins = get_subpage_content_from_page(page, language)

        context['list_plugins'] = list_plugins
        return context
        
plugin_pool.register_plugin(CollectionPlugin)
