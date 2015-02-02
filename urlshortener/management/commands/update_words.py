# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from optparse import make_option
from urlshortener.models import Word

import os
import re


class Command(BaseCommand):
    args = '--file <inputfile>'
    help = 'Update words from text file'

    option_list = BaseCommand.option_list + (
        make_option('--file',
            dest='file',
            default='urlshortener/words.txt',
            help='Custom input file'),
        )

    def handle(self, *args, **options):
        # Connect to database

        if options['file']:
            file_path = options['file']
            if not os.path.exists(file_path):
                raise CommandError(u'Input file not exists. ("%s")\n' % file_path)

        try:
            word_file = open(file_path, 'r')
        except Exception, e:
            self.stdout.write(u"Can't open input file. ('%s') Error: %s \n" % (file_path, str(e)))

        word_list = []
        for line in word_file:
            word = line.replace(' ', '')  # Remove blankspaces
            word = word.strip()  # Remove end of line characters
            word = word.lower()  # Make word lowercase
            word = re.sub(r'[\W_]', '', word)  # Remove symbols

            new_word, created = Word.objects.get_or_create(name=word)
            if created:  # Used to avoid repeated words
                word_list.append(word)

            self.stdout.write(u"Word Analyzed: '%s' " % line.strip())

        objs = [  # Used bulk to improve update speed
            Word(name=w)
            for w in word_list
        ]

        Word.objects.bulk_create(objs)

        self.stdout.write(u"Updated all new words !")
