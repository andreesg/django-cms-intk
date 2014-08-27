from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page

from .models import RichPage, RichSlideshow

class RichPageAdmin(PageExtensionAdmin):
	pass

class RichSlideshowAdmin(PageExtensionAdmin):
    pass

admin.site.register(RichPage, RichPageAdmin)
admin.site.register(RichSlideshow, RichSlideshowAdmin)
