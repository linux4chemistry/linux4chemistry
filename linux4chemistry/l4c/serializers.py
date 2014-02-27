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

    license_model = serializers.PrimaryKeyRelatedField(read_only=True)
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Software
        fields = (
            'id', 'name', 'url', 'license_model', 'open_source_info', 
            'categories', 'other_categories', 'description'
            )
