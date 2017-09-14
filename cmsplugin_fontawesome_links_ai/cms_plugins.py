# -*- coding: utf-8 -*-
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .forms import FontAwesomeLinkFormSet, FontAwesomeLinkCustomForm
from .models import Links, FontAwesomeLink


class FontAwesomeLinkAdmin(admin.StackedInline):
    model = FontAwesomeLink
    form = FontAwesomeLinkCustomForm
    formset = FontAwesomeLinkFormSet
    extra = 1


class FontAwesomeLinksPlugin(CMSPluginBase):
    model = Links
    name = _("FontAwesome Links")
    change_form_template = "cmsplugin_fontawesome_links_ai/admin/custom_form.html"
    render_template = "cmsplugin_fontawesome_links_ai/fontawesome_links.html"
    inlines = (FontAwesomeLinkAdmin,)


plugin_pool.register_plugin(FontAwesomeLinksPlugin)
