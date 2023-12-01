import datetime

from rest_framework import status
from rest_framework.response import Response

from kids_shop.logger import logger


def time_checker(func):

    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        total_time = end_time - start_time
        logger.info(f'Function: {func.__name__} | Time: {total_time}')
        return result
    return wrapper


def split_value(value) -> tuple | int:
    parts = value.split('-')
    if len(parts) == 2:
        start_value, end_value = map(int, parts)
        return start_value, end_value
    else:
        single_value = int(parts[0])
        return single_value
    
    
def favorite_or_cart(
        request,
        product_id: int,
        profile_id: int,
        profile_repository,
        product_repository,
        repository,
        obj_serializer,
        quantity=None,
        is_shop=True
):
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
        obj = repository.get_obj(profile_id, product_id)
        if obj.exists():
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_400_BAD_REQUEST)


def get_products(request, profile_id: int, repository, obj_serializer) -> Response:
    obj = repository.get_all_products(profile_id)
    serializer = obj_serializer(obj, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)