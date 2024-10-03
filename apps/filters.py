from django_filters import FilterSet, NumberFilter, CharFilter

from apps.models import Product


# class ProductFilter(FilterSet):
#
#     min_price = NumberFilter(field_name="price", lookup_expr='gte')
#     max_price = NumberFilter(field_name="price", lookup_expr='lte')
#
#     class Meta:
#         model = Product
#         fields = ['name']


class ProductFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name']