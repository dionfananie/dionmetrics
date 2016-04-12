from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'oauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('^login/$', 'twitterauth.views.twitter_signin', name='login'),
	url('^return/$', 'twitterauth.views.twitter_return', name='return'),
]
