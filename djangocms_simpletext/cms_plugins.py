# -*- coding: utf-8 -*-

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import SimpleText

class SimpleTextPlugin(CMSPluginBase):
    model = SimpleText
    name = _("Simple Text")
    render_template = "djangocms_simpletext/base.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder
        })
        return context
        
plugin_pool.register_plugin(SimpleTextPlugin)
