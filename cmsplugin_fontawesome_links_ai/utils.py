# -*- coding: utf-8 -*-
import os
import yaml

PATH = os.path.join(os.path.dirname(__file__), 'static/cmsplugin_fontawesome_links_ai/yaml/icons.yml')

def get_icon_choices():

    ICON_CHOICES = [('', '----------')]

    with open(PATH) as f:
        icons = yaml.load(f)

    for icon in icons.get('icons'):
        ICON_CHOICES.append((
            icon.get('id'),
            icon.get('name')
        ))

    return ICON_CHOICES
