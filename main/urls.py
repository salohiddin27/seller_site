from django.urls import path
from rest_framework.routers import DefaultRouter

from .SearchFilter import CategoryViewSet, ProductViewSet
from .views import category_products_list, category_list

router = DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)

urlpatterns = [
    path('category/', category_list, name='category'),

    path('category/<int:category_id>/', category_products_list, name='category_products')

]