from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'linux4chemistry.views.home', name='home'),
    # url(r'^linux4chemistry/', include('linux4chemistry.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # provide access to the CCL rss feed
    url(r'^ccl-rss/', include('cclfeed.urls')),

    # redirect everything to the app reimplementing the original site
    url(r'', include('oldsite.urls')),
)
