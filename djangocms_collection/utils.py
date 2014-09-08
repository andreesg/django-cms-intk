# -*- coding: utf-8 -*-

def get_subpage_content_from_page(page, language=None):
    plugins = []

    children = page.get_children()
    for child in children:
        child_plugins = child.placeholders.get(slot="content").get_plugins(language).order_by('-position').reverse()
        
        if len(child_plugins) > 0:
            #
            # TODO
            #
            try:
                picture = child_plugins[0]
                description = child_plugins[1]
                plugins.append({'instance':child, 'picture': picture, 'description': description})
            except:
                pass

    return plugins
        
