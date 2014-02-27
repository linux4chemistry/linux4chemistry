from django.conf.urls import patterns, url, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r'license_models', views.LicenseModelViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'softwares', views.SoftwareViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
