# -*- coding: utf-8 -*-
from django.forms import inlineformset_factory, ModelForm
from .models import Links, FontAwesomeLink
from .widgets import IconSelectWidget


class FontAwesomeLinkCustomForm(ModelForm):
    class Meta:
        model = FontAwesomeLink
        fields = ['icon', 'url', 'link_text']
        widgets = {
            'icon': IconSelectWidget(attrs={'class':'fontawesome-select', 'data-fontawesome-prefix':'fa'})
        }


FontAwesomeLinkFormSet = inlineformset_factory(Links, FontAwesomeLink, form=FontAwesomeLinkCustomForm)
