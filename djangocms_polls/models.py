from django.db import models
from polls.models import Poll
from cms.models import CMSPlugin
from django.contrib import admin

from cms.extensions import PageExtension
from cms.extensions import PageExtensionAdmin
from cms.extensions.extension_pool import extension_pool

class PollPluginModel(CMSPlugin):
	poll = models.ForeignKey(Poll)
	
	def __unicode__(self):
		return self.poll.question

class IconExtension(PageExtension):
	image = models.ImageField(upload_to='icons')

class IconExtensionAdmin(PageExtensionAdmin):
	pass

extension_pool.register(IconExtension)
admin.site.register(IconExtension, IconExtensionAdmin)


