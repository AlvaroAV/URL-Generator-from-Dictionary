# -*- coding: utf-8 -*-
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from urlshortener.models import *


@receiver(pre_delete, sender=URL)
def delete_content(sender, **kwargs):
    deleted_URL = kwargs['instance']
    word_name = deleted_URL.short_url

    word = Word.objects.get(name=word_name)
    word.used = False
    word.save()
