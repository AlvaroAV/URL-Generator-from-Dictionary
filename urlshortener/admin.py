# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *


class URLAdmin(admin.ModelAdmin):
    fields = ['original_url', 'short_url']
    list_display = ['original_url', 'short_url']

admin.site.register(URL, URLAdmin)


class WordAdmin(admin.ModelAdmin):
    fields = ['name', 'used']
    list_display = ['name', 'used']
    list_filter = ('used', )

admin.site.register(Word, WordAdmin)
