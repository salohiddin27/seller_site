from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from main.models import Category, Product
from main.serializers import CategorySerializers, ProductSerializers


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['category', 'is_discontinued']
    search_fields = ['name', 'price', 'description', 'brand']
    serializer_class = ProductSerializers