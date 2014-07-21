from django.db.models import Q
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
    model = Software
    serializer_class = SoftwareSerializer

    def get_queryset(self):
        # support filtering the Software queryset based on an optional 
        # subset of license models and/or software categories. 'other' 
        # can be used as a special software category identifier.

        queryset = self.model.objects.all()

        license_param = self.request.QUERY_PARAMS.get('license_model', '')
        license_models = set(license_param.split(',') if license_param else [])

        if license_models:
            queryset = queryset.filter(license_model__in=license_models)

        category_param = self.request.QUERY_PARAMS.get('category', '')
        categories = set(category_param.split(',') if category_param else [])

        other = 'other' in categories
        q1 = ~Q(other_categories='') if other else None

        categories.discard('other')
        q2 = Q(categories__in=categories) if categories else None

        if q1 and q2:
            queryset = queryset.filter(q1 | q2)
        elif q1:
            queryset = queryset.filter(q1)
        elif q2:
            queryset = queryset.filter(q2)

        return queryset.prefetch_related('categories')


