import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(
        field_name='category__name',
        lookup_expr='icontains'
    )
    
    class Meta:
        model = Product
        fields = ['name', 'category_name']