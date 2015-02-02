# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django import forms
from urlshortener.models import *


class URLForm(forms.Form):
    original_url = forms.URLField(label=_(u'Original URL'))

    def clean_original_url(self):
        data = self.cleaned_data['original_url']
        if URL.objects.filter(original_url=data):
            raise forms.ValidationError(_(u"This URL has been already created"))
        return data
