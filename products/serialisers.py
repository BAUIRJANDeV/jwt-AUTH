# products/serializers.py

from rest_framework import serializers
from .models import Category, Phone


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PhoneSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Phone
        fields = [
            'id',
            'name',
            'category',
            'category_id',
            'price',
            'description',
            'created_at',
            'updated_at'
        ]
