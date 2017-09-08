# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='FontAwesomeLink',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('icon', models.CharField(max_length=60)),
                ('url', models.URLField(max_length=250, blank=True, verbose_name='URL')),
                ('link_text', models.CharField(max_length=160, blank=True, verbose_name='link text')),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, serialize=False, to='cms.CMSPlugin', primary_key=True)),
                ('title', models.CharField(null=True, max_length=160, blank=True, verbose_name='FontAwesome links title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='fontawesomelink',
            name='plugin',
            field=models.ForeignKey(to='cmsplugin_fontawesome_links_ai.Links', verbose_name='Plugin', related_name='fontawesome_links'),
        ),
    ]
