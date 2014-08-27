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

    # Filters

    location_filter = models.CharField(max_length=100, default='/some_location/')
    sort_by_creation_date = models.BooleanField(_('Sort by creation date'), default=False)
    sort_by_modification_date = models.BooleanField(_('Sort by modification date'), default=False)
    reverse_dates = models.BooleanField(_('Reverse date'), default=False)

    def save(self, *args, **kwargs):
        self.location_filter = self.extended_object.get_absolute_url()
        super(RichCollection, self).save(*args, **kwargs)

    @property
    def get_richpages_by_filter(self):
        page = self.extended_object
        pages = page.get_children()

        if self.sort_by_creation_date:
            if self.reverse_dates:
                return pages.order_by('-publication_date').reverse()
            else:
                return pages.order_by('-publication_date')

        elif self.sort_by_modification_date:
            if self.reverse_dates:
                return pages.order_by('-changed_date').reverse()
            else:
                return pages.order_by('-changed_date')

        return pages

extension_pool.register(RichCollection)
