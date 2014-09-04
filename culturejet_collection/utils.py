# -*- coding: utf-8 -*-

def get_subpage_content_from_page(page, language=None):
    plugins = []

    children = page.get_children()
    for child in children:
        child_plugins = child.placeholders.get(slot="content").get_plugins(language).order_by('-position').reverse()
        if len(child_plugins):
            plugins.append({'instance':child, 'plugins': child_plugins})

    return plugins
        
