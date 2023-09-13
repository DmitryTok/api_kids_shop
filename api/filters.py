from django_filters import rest_framework as filters

from api.models import Product


class ProductFilter(filters.FilterSet):
    age = filters.CharFilter(method='filter_age')
    price = filters.CharFilter(method='filter_price')

    class Meta:
        model = Product
        fields = [
            'category__name',
            'section__name',
            'brand__name',
            'rating',
            'male',
            'color__name',
            'product_size__brand_size',
        ]

    def filter_age(self, queryset, name, value):
        try:
            age_parts = value.split('-')
            if len(age_parts) == 2:
                start_age, end_age = map(int, age_parts)
                return queryset.filter(age__range=(start_age, end_age))
            else:
                age = int(age_parts[0])
                return queryset.filter(age=age)
        except ValueError:
            return queryset.none()

    def filter_price(self, queryset, name, value):
        try:
            price_parts = value.split('-')
            if len(price_parts) == 2:
                start_price, end_price = map(int, price_parts)
                return queryset.filter(price__range=(start_price, end_price))
            else:
                price = int(price_parts[0])
                return queryset.filter(price=price)
        except ValueError:
            return queryset.none()
