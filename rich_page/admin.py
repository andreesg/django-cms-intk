from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page

from .models import RichPage

class RichPageAdmin(PageExtensionAdmin):
	pass

admin.site.register(RichPage, RichPageAdmin)
