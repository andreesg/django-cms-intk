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
	#title = models.CharField(_('Title'), max_length=255)
	#slug = models.CharField(_('Slug'), max_length=255, unique=True, blank=True,
    #                        help_text=_('Used in the URL. If changed, the URL will change. '
    #                                    'Clean it to have it re-created.'))
	key_visual = FilerImageField(verbose_name=_('Key Visual'), blank=True, null=True)
	lead_in = HTMLField(_('Lead-in'),
                        help_text=_('Will be displayed in lists, and at the start of the detail page (in bold)'))

	body = HTMLField(_('Body'),
                        help_text=_('Will be displayed in full page'))
	
	tags = TaggableManager(blank=True)

	# def save(self, **kwargs):
	# 	if not self.slug:
	# 		self.slug = slugify(self.title)
	# 	return super(RichPage, self).save(**kwargs)

extension_pool.register(RichPage)
