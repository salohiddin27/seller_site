from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models import Category, Product
from .serializers import CategorySerializers, ProductSerializers


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    filter_backends = [DjangoFilterBackend]


def category_list(request):
    search = request.GET.get('search')
    category = Category.objects.all()
    if search:
        category = category.filter(name__icontains=search)

    return render(request, 'category_list.html',
                  {'category': category,
                   'search': search,
                   })


def category_products_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    search = request.GET.get('search')
    products = Product.objects.filter(category=category)
    if search:
        products = products.filter(name__icontains=search)

    return render(request, 'products.html',
                  {'category': category,
                   'products': products,
                   'search': search,
                   })


