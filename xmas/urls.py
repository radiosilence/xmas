from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^card/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$',
        'xmas.views.card', name='card'),
    # url(r'^xmas/', include('xmas.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
