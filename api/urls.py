from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'products', views.ProductListView)
router.register(r'pictures', views.PictureListView)
router.register(r'category', views.CategoryListView)
router.register(r'section', views.SectionListView)
router.register(r'brand', views.BranListView)
router.register(r'favorite', views.FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
