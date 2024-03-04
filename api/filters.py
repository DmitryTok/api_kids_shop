import operator
from functools import reduce

from django.db.models import Q
from django_filters import rest_framework as filters

from api.models import Brand, Category, Product, Section


def split_value(value: str) -> tuple | int:
    parts = value.split('-')
    if len(parts) == 2:
        start_value, end_value = map(int, parts)
        return start_value, end_value
    else:
        single_value = int(parts[0])
        return single_value


class ProductFilter(filters.FilterSet):
    age = filters.NumberFilter(label='int', method='filter_age')
    price = filters.NumberFilter(method='filter_price')
    name = filters.CharFilter(label='str', method='filter_name')
    category = filters.CharFilter(label='str', method='filter_category_name')
    brand = filters.CharFilter(label='str', method='filter_brand_name')
    section = filters.CharFilter(label='str', method='filter_section_name')

    class Meta:
        model = Product
        fields = []

    @staticmethod
    def filter_age(queryset, name, value):
        try:
            return queryset.filter(
                attributes__attribute_name='Age',
                attributes__value__icontains=value,
            )
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_price(queryset, name, value):
        try:
            return queryset.filter(price__icontains=value)
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
            names = [
                Q(brand__name__icontains=brand) for brand in value.split(', ')
            ]
            return queryset.filter(reduce(operator.or_, names))
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_category_name(queryset, name, value):
        try:
            names = [
                Q(category__name__icontains=category)
                for category in value.split(', ')
            ]
            return queryset.filter(reduce(operator.or_, names))
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_section_name(queryset, name, value):
        try:
            names = [
                Q(section__name__icontains=section)
                for section in value.split(', ')
            ]
            return queryset.filter(reduce(operator.or_, names))
        except ValueError:
            return queryset.none()


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter(label='str', method='filter_name')

    class Meta:
        model = Category
        fields = []

    @staticmethod
    def filter_name(queryset, name, value):
        try:
            names = [
                Q(name__icontains=category) for category in value.split(', ')
            ]
            return queryset.filter(reduce(operator.or_, names))
        except ValueError:
            return queryset.none()


class SectionFilter(filters.FilterSet):
    name = filters.CharFilter(label='str', method='filter_name')

    class Meta:
        model = Section
        fields = []

    @staticmethod
    def filter_name(queryset, name, value):
        try:
            return queryset.filter(name__icontains=value)
        except ValueError:
            return queryset.none()


class BrandFilter(filters.FilterSet):
    name = filters.CharFilter(label='str', method='filter_name')

    class Meta:
        model = Brand
        fields = []

    @staticmethod
    def filter_name(queryset, name, value):
        try:
            return queryset.filter(name__icontains=value)
        except ValueError:
            return queryset.none()
