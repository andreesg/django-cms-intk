from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from taggit.managers import TaggableManager
from cms.models.pagemodel import Page
from cms.extensions import PageExtension
from cms.extensions.extension_pool import extension_pool

class RichPage(PageExtension):
	key_visual = FilerImageField(verbose_name=_('Lead Image'), blank=True, null=True)
	lead_in = HTMLField(_('Lead-in'),
                        help_text=_('Will be displayed in lists, and at the start of the detail page (in bold)'), default="Your lead in text")

	body = HTMLField(_('Body'),
                        help_text=_('Will be displayed in full page'), default="Your body text")
	
	tags = TaggableManager(blank=True)

def _get_pages_by_filter(obj):
    pages = obj.get_children()
    return pages

Page._get_pages_by_filter = _get_pages_by_filter
Page.get_pages_by_filter = property(lambda u: u._get_pages_by_filter)


extension_pool.register(RichPage)
