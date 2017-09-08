# -*- coding: utf-8 -*-
from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Links(CMSPlugin):
    title = models.CharField(verbose_name=_("FontAwesome links title"), max_length=160, blank=True, null=True)

    def __str__(self):
        return self.title or ""

    def copy_relations(self, oldinstance):
        for link in oldinstance.fontawesome_links.all():
            link.pk = None
            link.id = None
            link.plugin = self
            link.save(force_insert=True)


class FontAwesomeLink(models.Model):
    plugin = models.ForeignKey(Links, verbose_name=_("Plugin"), related_name="fontawesome_links")
    icon = models.CharField(max_length=60)
    url = models.URLField(_('URL'), max_length=250, blank=True)
    link_text = models.CharField(verbose_name=_("link text"), max_length=160, blank=True)
