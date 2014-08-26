from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from taggit.managers import TaggableManager
from cms.models.pagemodel import Page
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool
from django import forms

class RichCollection(PageExtension):
    lead_in = HTMLField(_('Lead-in'), help_text=_('Will be displayed in lists, and at the start of the detail page (in bold)'), default="Your lead in text")
    body = HTMLField(_('Body'), help_text=_('Will be displayed in full page'), default="Your body text")
    location_filter = models.CharField(max_length=100, default='/some_location/')

    @property
    def get_richpages_by_filter(self):
        page = self.extended_object
        pages = page.get_children()
        return pages

#RichCollection._get_richpages_by_filter = _get_richpages_by_filter
#RichCollection.get_richpages_by_filter = property(lambda u: u._get_richpages_by_filter)

extension_pool.register(RichCollection)
