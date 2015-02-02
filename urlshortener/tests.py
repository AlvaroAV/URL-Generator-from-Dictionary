from django.test import TestCase
from urlshortener.utils import *
from urlshortener.models import Word, URL


class HomeTestCase(TestCase):
    def test_index(self):
        ''' Test if index is loaded correctly '''
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        print '\n-- Access granted for Index\n'


class RedirectionTestCase(TestCase):
    ''' Test if redirection using a word works well '''
    def setUp(self):
        Word.objects.create(name="test1")
        URL.objects.create(original_url=u"http://www.google.com", short_url='test1')

    def test_redirection(self):
        resp = self.client.get('/test1/')
        self.assertEqual(resp.status_code, 302)
        print '\n-- Redirection worked, returns 302\n'


class WordTestCase(TestCase):
    ''' Test unicode function '''
    def setUp(self):
        Word.objects.create(name="test1")

    def test_unicode(self):
        test1 = Word.objects.get(name="test1")

        print '\n-- Success printing short-url: %s\n' % test1


class getWordTestCase(TestCase):
    ''' Test get_word function '''
    def setUp(self):
        Word.objects.create(name="test1")
        Word.objects.create(name="customword")

    def test_customword(self):
        word = get_word('http://www.customword.com')
        self.assertEqual(word, 'customword')
        print '\n-- Success ! Returns valid word for URL'
