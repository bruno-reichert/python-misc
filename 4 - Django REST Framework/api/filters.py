import django_filters
from api.models import Product
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