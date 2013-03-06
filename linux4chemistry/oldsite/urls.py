from django.conf.urls import patterns, include, url

from . import views

urlpatterns = patterns('',
  url(r'^comment/$', 
      views.LeaveCommentView.as_view(), name='leave_comment'),
  url(r'^definition/$', 
      views.LicenseDefinitionView.as_view(), name='license_definition'),
  url(r'^$', 
      views.Linux4ChemistryView.as_view(), name='linux4chemistry'),
)
