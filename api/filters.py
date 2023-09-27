from django_filters import rest_framework as filters

from api.models import Product
from api.utils import split_value


class ProductFilter(filters.FilterSet):
    age_range = filters.CharFilter(method='filter_age')
    price_range = filters.CharFilter(method='filter_price')

    class Meta:
        model = Product
        fields = [
            'category__name',
            'section__name',
            'brand__name',
            'rating',
            'male',
        ]

    @staticmethod
    def filter_age(queryset, name, value):
        try:
            return queryset.filter(age__range=(split_value(value)))
        except ValueError:
            return queryset.none()

    @staticmethod
    def filter_price(queryset, name, value):
        try:
            return queryset.filter(price__range=(split_value(value)))
        except ValueError:
            return queryset.none()
