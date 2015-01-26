from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

import django.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'youth_paper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('fdyouth.urls')),
    url(r'', include('subscribe.urls')),
    url(r'^js/(?P<path>.*)$','django.views.static.serve',
        {'document_root':'./static/js/',
         'show_indexes':True}),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':'./static/css/',
         'show_indexes':True}),
    url(r'^image/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':'./static/image/',
        'show_indexes':True}),
    url(r'^iframe/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':'./static/iframe',
         'show_indexes':True}),
    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':'./static/fonts', 'show_indexes':True})
    )
