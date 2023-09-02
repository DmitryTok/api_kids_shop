from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (BranListView, CategoryListView, FavoriteViewSet,
                       OnSaleProductView, PictureListView, ProductListView,
                       SectionListView, ShoppingCartViewSet, TOPProductView)

router = DefaultRouter()
router.register(r'products', ProductListView)
router.register(r'pictures', PictureListView)
router.register(r'category', CategoryListView)
router.register(r'section', SectionListView)
router.register(r'brand', BranListView)
router.register(r'favorite', FavoriteViewSet)
router.register(r'top', TOPProductView)
router.register(r'on_sale', OnSaleProductView)
router.register(r'shopping_cart', ShoppingCartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
