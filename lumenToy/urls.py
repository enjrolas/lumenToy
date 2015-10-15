from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^incoming', 'recording.views.incoming', name='recording'),
     url(r'^recordingComplete', 'recording.views.recordingComplete', name='recordingComplete'),
    # url(r'^g/', include('recording.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
