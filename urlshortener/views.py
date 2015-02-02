# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.template import RequestContext

from urlshortener.models import URL, Word
from forms import URLForm
from utils import get_word


def url_redirect(request, short_url):
    ''' Redirect to a URL based on the word '''
    try:  # Try to get the URL object if exists
        url_object = URL.objects.get(short_url=short_url)
        redirect_url = url_object.original_url
    except:
        redirect_url = ""

    if short_url == "" or redirect_url == "":
        msg = '<h1>URL %s not found</h1>' % (short_url,)
        return HttpResponseNotFound(msg)
    else:
        # Redirect to original URL
        return HttpResponseRedirect(redirect_url)


def home(request):
    ''' Index URL used to create short url's '''
    error = u''
    success = False

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']

            # Get a word based on the URL
            word = get_word(original_url)

            if not word:
                error = _(u"Can't find word for original_url='%s'" % original_url)
                return render_to_response('home.html', {'error': error}, context_instance=RequestContext(request))

            try:  # Try to create URL and change word used status
                shorten_url = URL(original_url=original_url, short_url=word)
                shorten_url.save()

                used_word = Word.objects.get(name=word)
                used_word.used = True
                used_word.save()

                success = True
            except Exception, e:
                error = _(u"Can't create url, Error='%s'" % str(e))
                return render_to_response('home.html', {'error': error}, context_instance=RequestContext(request))
    else:
        form = URLForm()

    return render_to_response('home.html', {'error': error, 'form': form, 'success': success}, context_instance=RequestContext(request))
