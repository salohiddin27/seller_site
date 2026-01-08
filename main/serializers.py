from rest_framework import serializers

from .models import Category, Product


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    created_at = serializers.DateTimeField(format="%d %B %Y, %H:%M:%S")
