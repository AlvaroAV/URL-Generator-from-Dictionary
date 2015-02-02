from urlshortener.models import Word, URL

import re
import random


def get_word(original_url):
    ''' Get word based on URL '''
    final_word = ''
    original_url = re.split('[\W_]', original_url)  # Split original URL's using symbols
    forbidden_words = ['www', 'http', 'https']

    possible_words = []
    for word in original_url[:-1]:
        if word in forbidden_words or not word:
            continue

        word = word.replace(' ', '')  # Remove blankspaces
        word = word.lower()  # Make word lowercase
        word = word.strip()  # Remove end of line characters
        word = re.sub(r'[\W_]', '', word)  # Remove symbols
        word = re.sub(r'\d+', '', word)  # Remove numbers

        for w in Word.objects.filter(name=word, used=False):
            possible_words.append(w.name)

    # Here possible_words should contain valid words
    if possible_words:
        final_word = random.choice(possible_words)
    else:  # Couldn't find any possible word
        possible_words = Word.objects.filter(used=False)

        if possible_words:
            final_word = random.choice(possible_words)
        else:  # All words are used
            # Get oldest URL
            oldest_url = URL.objects.all().order_by('-created')[0]
            final_word = oldest_url.short_url

            oldest_url.delete()

    return final_word
