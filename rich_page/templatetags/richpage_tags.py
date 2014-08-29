# -*- coding: utf-8 -*-
from classytags.arguments import Argument
from classytags.core import Options
from classytags.helpers import InclusionTag, AsTag
from django import template
from django.template import RequestContext
from django.shortcuts import render_to_response
from cms.utils import get_language_from_request
from cms.api import get_page_draft

register = template.Library()

@register.inclusion_tag('rich_page/templatetags/richpage_content.html', name='include_richpage_content', takes_context=True)
def IncludeRichPageContent(context):
    request = context['request']
    lang = get_language_from_request(request)
    
    is_collection = False
    is_richpage = False

    page = get_page_draft(request.current_page)

    title_page = page.title_set.get(language=lang)

    print title_page

    return render_to_response('rich_page/templatetags/richpage_content.html', { 'title_page': title_page.richpage }, context_instance=context)


