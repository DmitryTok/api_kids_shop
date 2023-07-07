from http import HTTPStatus

from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from kids_shop.permissions import IsAdminOrReadOnly


class BaseRetrieveViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = LimitOffsetPagination

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Http404:
            message = {'Error': 'Object does not exist'}
            return JsonResponse(message, status=HTTPStatus.BAD_REQUEST)
