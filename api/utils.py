import inspect
from typing import Any

from django.http import HttpRequest
from rest_framework import status
from rest_framework.response import Response

from api import filters


def check_obj(
    repository, profile_id, product_id
) -> Response | None:
    if repository.get_obj(profile_id, product_id).exists():
        return Response(
            {'error': 'This product already added'},
            status=status.HTTP_400_BAD_REQUEST,
        )


def is_shop_check(
    product,
    profile,
    profile_id,
    product_id,
    repository: object | Any,
    is_shop: bool = None,
    quantity: int = None,
) -> Response:
    response = check_obj(
        product_id=product_id,
        profile_id=profile_id,
        repository=repository
    )
    if response:
        return response
    if is_shop:
        return repository.create_obj(profile, product, quantity)
    else:
        return repository.create_obj(profile, product)


def favorite_or_cart(
    request: HttpRequest,
    product_id: int,
    profile_id: int,
    profile_repository: object | Any,
    product_repository: object | Any,
    repository: object | Any,
    obj_serializer: object | Any,
    quantity: int = None,
    is_shop=True,
) -> Response:
    profile = profile_repository.get_obj(profile_id)
    product = product_repository.get_obj(product_id)

    if request.method == 'POST':
        quantity = request.data.get('quantity')
        if (
                profile.id != request.data.get('profile') or
                product.id != request.data.get('product')
        ):
            return Response(
                {'error': 'Provided data does not match'},
                status=status.HTTP_400_BAD_REQUEST
            )
        obj = is_shop_check(
            profile=profile,
            product=product,
            profile_id=profile_id,
            product_id=product_id,
            repository=repository,
            is_shop=is_shop,
            quantity=quantity,
        )
        if isinstance(obj, Response):
            return obj
        serializer = obj_serializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':
        if is_shop is True:
            obj = repository.get_obj(profile_id, product_id)
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
    obj_serializer: object | Any,
) -> Response:
    obj = repository.get_all_products(profile_id)
    serializer = obj_serializer(obj, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


def store_filters() -> dict[dict[str, str]]:
    result = {}

    filter_classes = [
        obj
        for name, obj in inspect.getmembers(filters)
        if inspect.isclass(obj)
    ]

    api_filter_modules = [
        obj for obj in filter_classes if obj.__module__ == 'api.filters'
    ]

    for filter_class in api_filter_modules:
        meta = getattr(filter_class, 'Meta', None)
        if meta:
            model = getattr(meta, 'model', None)
            if model:
                declared_filters = getattr(
                    filter_class, 'declared_filters', None
                )
                if declared_filters:
                    filter_info = {
                        name: filter_instance.label
                        for name, filter_instance in declared_filters.items()
                    }
                    result[model.__name__] = filter_info

    return result
