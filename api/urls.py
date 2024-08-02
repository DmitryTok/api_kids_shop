from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (BranListView, CategoryListView, PictureListView,
                       ProductListView, OrderListView, api_filters)

router = DefaultRouter()
router.register(r'products', ProductListView)
router.register(r'pictures', PictureListView)
router.register(r'category', CategoryListView)
router.register(r'brand', BranListView)
router.register(r'orders', OrderListView)

urlpatterns = [
    path('', include(router.urls)),
    path('filters/', api_filters, name='api_filters'),
]
