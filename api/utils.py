from typing import Any

from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response


def split_value(value) -> tuple | int:
    parts = value.split('-')
    if len(parts) == 2:
        start_value, end_value = map(int, parts)
        return start_value, end_value
    else :
        single_value = int(parts[0])
        return single_value


def favorite_or_cart(
        request: HttpRequest,
        product_id: int,
        profile_id: int,
        profile_repository: object | Any,
        product_repository: object | Any,
        repository: object | Any,
        obj_serializer: object | Any,
        quantity: int = None,
        is_shop=True
) -> Response:
    profile = profile_repository.get_obj(profile_id)
    product = product_repository.get_obj(product_id)
    
    if request.method == 'POST':
        if repository.get_obj(
                profile_id,
                product_id).exists():
            return Response(
                {'error': 'This product already added'},
                status=status.HTTP_400_BAD_REQUEST
            )
        if is_shop is True:
            obj = repository.create_obj(profile, product, quantity)
            serializer = obj_serializer(obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            obj = repository.create_obj(profile, product)
            serializer = obj_serializer(obj)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    if request.method == 'DELETE':
        if is_shop is True:
            obj = repository.get_obj(profile_id, product_id, quantity)
        else:
            obj = repository.get_obj(profile_id, product_id)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get_products(
        request: HttpRequest,
        profile_id: int,
        repository: object | Any,
        obj_serializer: object | Any
) -> Response:
    obj = repository.get_all_products(profile_id)
    serializer = obj_serializer(obj, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
