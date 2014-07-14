from django.conf.urls import patterns, include, url

from views import LatestMessagesFeed

urlpatterns = patterns('',
    url(r'^$', LatestMessagesFeed()),
)