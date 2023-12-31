from http import HTTPStatus

from django.http import Http404, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from kids_shop.permissions import IsAdminOrReadOnly


class BaseRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAdminOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            message = {'Error': 'Object does not exist'}
            return JsonResponse(message, status=HTTPStatus.BAD_REQUEST)
