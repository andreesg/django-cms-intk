# -*- coding: utf-8 -*-

from django.contrib import admin
from cms.extensions import PageExtensionAdmin
from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page

from .models import RichCollection

class RichCollectionAdmin(PageExtensionAdmin):
	pass

admin.site.register(RichCollection, RichCollectionAdmin)
