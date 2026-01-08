from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .SearchFilter import CategoryViewSet, ProductViewSet
from .views import category_products_list, category_list, add_to_cart, cart_view_json, remove_from_cart

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('categories/', category_list, name='categories'),

    path('category/<int:category_id>/', category_products_list, name='category_products'),

    path('cart/add/<int:product_id>/', add_to_cart, name='cart_item'),
    path('cart/view-json/', cart_view_json, name='cart_view_json'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_basket'),
    path('', include(router.urls)),
]
