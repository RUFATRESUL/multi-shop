import django_filters as filters
from .models import Prouduct
class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price',lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price',lookup_expr='lte')

    class Meta:
        model = Prouduct
        fields = ['sizes', 'colors','category']