from rest_framework import viewsets

from .models import LicenseModel, Category, Software
from .serializers import (
    LicenseModelSerializer, CategorySerializer, SoftwareSerializer
    )


class LicenseModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LicenseModel.objects.all()
    serializer_class = LicenseModelSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SoftwareViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Software.objects.all()
    serializer_class = SoftwareSerializer
    

