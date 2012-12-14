from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^card/$', 'xmas.views.card', name='card'),
    # url(r'^xmas/', include('xmas.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
