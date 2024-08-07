from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserView, ProfileViewSet, AddressViewSet

router = DefaultRouter()

router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'custom_delete_user', CustomUserView, basename='user_delete')
router.register(r'address', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
