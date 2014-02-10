from django.conf import settings
from django.conf.urls import patterns, include, url

if 'django.contrib.admin' in settings.INSTALLED_APPS:
    from django.contrib import admin
    admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linux4chemistry.views.home', name='home'),
    # url(r'^linux4chemistry/', include('linux4chemistry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # provide access to the CCL rss feed
    url(r'^ccl-rss/', include('cclfeed.urls')),

    # redirect everything to the app reimplementing the original site
    url(r'', include('oldsite.urls')),
)

if 'django.contrib.admin' in settings.INSTALLED_APPS:

    urlpatterns += patterns('',
        url(r'^admin/', include(admin.site.urls)),
    )
