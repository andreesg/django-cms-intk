# -*- coding: utf-8 -*-

def get_subpage_content_from_page(page, language=None):
    plugins = []

    children = page.get_children()
    for child in children:
        plugins.append({'instance':child, 'plugins':child.placeholders.get(slot="content").get_plugins().order_by('-position').reverse()})

    return plugins
        
