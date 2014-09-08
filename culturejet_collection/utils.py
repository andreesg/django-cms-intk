# -*- coding: utf-8 -*-

def get_subpage_content_from_page(page, language=None):
    plugins = []

    children = page.get_children()
    for child in children:
        if child.publication_date:
            
            child_plugins = child.placeholders.get(slot="content").get_plugins(language).order_by('-position').reverse()
            
            if len(child_plugins) > 0:
                # TODO
                try:
                    filer_plugin = child_plugins.filter(plugin_type='FilerImagePlugin')[0]
                    simpletext_plugin = child_plugins.filter(plugin_type='SimpleTextPlugin')[0]
                    picture = filer_plugin.get_plugin_instance()[0].image
                    description = simpletext_plugin
                    plugins.append({'instance':child, 'picture': picture, 'description': description})
                except:
                    pass

    return plugins

