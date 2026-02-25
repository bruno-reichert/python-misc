import django_filters
from api.models import Product, Order
from rest_framework import filters

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['icontains'], # Permite filtrar por nome usando query params, ex: /api/products/?name=example
            'price': ['exact', 'lt', 'gt', 'range'], # Permite filtrar por preço usando query params, ex: /api/products/?price=10 ou /api/products/?price__lt=10 ou /api/products/?price__gt=10 ou /api/products/?price__range=10,20 
        }

class InStockFilterBackEnd(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(stock__gt=0)

class OrderFilter(django_filters.FilterSet):
    created_at = django_filters.DateTimeFilter(field_name='created_at__date')
    class Meta:
        model = Order
        fields = {
            'status': ['exact'], # Permite filtrar por status usando query params, ex: /api/orders/?status=Pending
            'created_at': ['lt', 'gt', 'exact'] # Permite filtrar por data de criação usando query params, ex: /api/orders/?created_at__lt=2024-01-01 ou /api/orders/?created_at__gt=2024-01-01 ou /api/orders/?created_at=2024-01-01
        }