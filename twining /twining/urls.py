from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twinapp.views.base'),
    url(r'^help/$', 'twinapp.views.help'),
    url(r'^about/$', 'twinapp.views.about'),
    #url(r'^base/', 'twinapp.views.base'),
    url(r'^search_result/', 'twinapp.views.search_result'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
)
