from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

urlpatterns = patterns('',
    url(r'^', include('apps.users.urls')),
    url(r'^', include('apps.classes.urls')),

    
    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static2/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
    )
