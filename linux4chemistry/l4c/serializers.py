from rest_framework import serializers

from .models import LicenseModel, Category, Software


class LicenseModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = LicenseModel
        fields = ('label', 'name')


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('label', 'name')


class SoftwareSerializer(serializers.ModelSerializer):

    #categories
    #license_model

    class Meta:
        model = Software
        fields = (
            'id', 'name', 'url', 'other_categories',
            'open_source_info', 'description'
            )
