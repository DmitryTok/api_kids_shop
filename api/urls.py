from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (BranListView, CategoryListView, OnSaleProductView,
                       PictureListView, ProductListView, ShoppingCartViewSet,
                       TOPProductView, api_filters)

router = DefaultRouter()
router.register(r'products', ProductListView)
router.register(r'pictures', PictureListView)
router.register(r'category', CategoryListView)
router.register(r'brand', BranListView)
router.register(r'top', TOPProductView)
router.register(r'on_sale', OnSaleProductView)
router.register(r'shopping_cart', ShoppingCartViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('filters/', api_filters, name='api_filters'),
]
