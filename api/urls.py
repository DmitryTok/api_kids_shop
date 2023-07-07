from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CategoryListView, PictureListView, ProductListView, SectionListView

router = DefaultRouter()
router.register(r'products', ProductListView)
router.register(r'pictures', PictureListView)
router.register(r'category', CategoryListView)
router.register(r'section', SectionListView)

urlpatterns = [
    path('', include(router.urls)),
]
