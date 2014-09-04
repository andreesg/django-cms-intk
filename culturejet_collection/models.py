# -*- coding: utf-8 -*-

from cms.models.pluginmodel import CMSPlugin

from django.db import models
    
class Collection(CMSPlugin):
    name = models.CharField(max_length=50, default='Collection')


