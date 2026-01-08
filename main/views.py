from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from main.models import Category, Product, Cart
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
    categories = Category.objects.all()
    if search:
        categories = categories.filter(name__icontains=search)

    return render(request, 'category_list.html',
                  {'categories': categories,
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


@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        else:
            cart_item.save()
        return JsonResponse({
            "message": f"1 ta {product.name} savatga qo‘shildi",
            "quantity": cart_item.quantity
        })
    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def cart_view_json(request):
    cart_items = Cart.objects.filter(user=request.user)
    data = {
        "cart_items": [
            {
                "id": item.id,
                "product": {

                    "name": item.product.name,
                    "price": item.product.price,
                    "photo_url": item.product.photo.url

                },
                "quantity": item.quantity,
                "total": item.product.price * item.quantity

            }
            for item in cart_items
        ],
        "cart_count": cart_items.count(),
        "total_price": sum(item.product.price * item.quantity for item in cart_items)
    }
    return JsonResponse(data)


@login_required
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
        cart_item.delete()
        return JsonResponse({"message": "Mahsulot savatdan o‘chirildi"})
    return JsonResponse({"error": "Invalid request"}, status=400)
