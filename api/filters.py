import operator
from functools import reduce

from django.db.models import Q
from django_filters import rest_framework as filters

from api.models import Product
from api.utils import split_value


class ProductFilter(filters.FilterSet):
    age = filters.CharFilter(method='filter_age')
    price = filters.CharFilter(method='filter_price')
    name = filters.CharFilter(method='filter_name')
    category = filters.CharFilter(method='filter_category_name')
    brand = filters.CharFilter(method='filter_brand_name')
    section = filters.CharFilter(method='filter_section_name')

    class Meta:
        model = Product
        fields = [
            'rating',
            'male',
        ]

    @staticmethod
    def filter_age(queryset, name, value):
        try:
            return queryset.filter(age__range=split_value(value))
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_price(queryset, name, value):
        try:
            return queryset.filter(price__range=(split_value(value)))
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_name(queryset, name, value):
        try:
            names = [Q(name__icontains=product) for product in value.split()]
            return queryset.filter(reduce(operator.and_, names))
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_brand_name(queryset, name, value):
        try:
            return queryset.filter(brand__name__icontains=value)
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_category_name(queryset, name, value):
        try:
            return queryset.filter(category__name__icontains=value)
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_section_name(queryset, name, value):
        try:
            return queryset.filter(section__name__icontains=value)
        except ValueError:
            return queryset.none()
