# from django_filters import rest_framework as filters
#
# from api.models import Product
#
#
# class ProductFilter(filters.FilterSet):
#     age_range = filters.CharFilter(method='filter_diapason')
#     price_range = filters.CharFilter(method='filter_diapason')
#
#     class Meta:
#         model = Product
#         fields = [
#             'category__name',
#             'section__name',
#             'brand__name',
#             'rating',
#             'male',
#             'color__name',
#             'product_size__brand_size',
#         ]
#
#     def filter_diapason(self, queryset, name, value):
#         try:
#             parts = value.split('-')
#             if len(parts) == 2:
#                 start_value, end_value = map(int, parts)
#                 if name == 'age_range':
#                     return queryset.filter(age__range=(start_value, end_value))
#                 elif name == 'price_range':
#                     return queryset.filter(price__range=(start_value, end_value))
#             else:
#                 single_value = int(parts[0])
#                 if name == 'age_range':
#                     return queryset.filter(age=single_value)
#                 elif name == 'price_range':
#                     return queryset.filter(price=single_value)
#         except ValueError:
#             return queryset.none()
