# -*- coding: utf-8 -*-

from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from cms.utils.compat.dj import python_2_unicode_compatible
from django.db import models
    
@python_2_unicode_compatible
class SimpleText(CMSPlugin):
    text = models.TextField(_('Text'), blank=True, null=True)

    search_fields = ('text',)

    def __str__(self):
        return self.text


