# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import *
from settings import DOMAIN


class Word(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name=_(u'Name'))
    used = models.BooleanField(default=False, verbose_name=_(u'Used'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _(u'Word')
        verbose_name_plural = _(u'Words')


class URL(models.Model):
    original_url = models.URLField(max_length=2048, verbose_name=_(u'Original URL'))
    short_url = models.CharField(max_length=255, unique=True, verbose_name=_(u'Short URL'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation date'))

    def __unicode__(self):
        return self.original_url

    class Meta:
        verbose_name = _(u'URL')
        verbose_name_plural = _(u'URLs')

    def get_shortURL(self):  # Used to return a link with the shorten URL
        return format_html("<a href={0}{1}>{0}{1}</a>", DOMAIN, self.short_url)
    get_shortURL.short_description = _(u'Short URL')

    def get_URL(self):  # Used to return a link with the original URL
        return format_html("<a href={0}>{0}</a>", self.original_url)
    get_URL.short_description = _(u'Original URL')
