from django.conf.urls import patterns, include, url
from django.contrib import admin
from urlshortener import views
admin.autodiscover()

urlpatterns = patterns('',
    # Index URL
    url(r'^/?$', views.home, name='home'),

    # Admin URL
    url(r'^admin/', include(admin.site.urls)),

    # Redirect URL
    url(r'^(?P<short_url>\w+)/?$', views.url_redirect, name='url_redirect'),
    
)
