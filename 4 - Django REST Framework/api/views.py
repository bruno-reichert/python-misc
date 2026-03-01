from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Max
from django.shortcuts import get_object_or_404, render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.pagination import (LimitOffsetPagination,
                                       PageNumberPagination)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api import models
from api.filters import InStockFilterBackEnd, OrderFilter, ProductFilter
from api.models import Order, OrderItem, Product, User
from api.serializers import (OrderSerializer, ProductInfoSerializer,
                             ProductSerializer, OrderCreateSerializer, UserSerializer)

# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('pk')
    serializer_class = ProductSerializer
    filterset_class = ProductFilter # Permite filtrar por nome e preço usando query params, ex: /api/products/?name=example&price=10
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter, InStockFilterBackEnd] # Permite filtrar e buscar usando query params
    search_fields = ['=name', 'description'] # Permite buscar por nome e descrição usando query params, ex: /api/products/?search=example
    ordering_fields = ['price', 'name'] # Permite ordenar por preço e nome usando query params, ex: /api/products/?ordering=price ou /api/products/?ordering=-price
    pagination_class = None # Permite paginar os resultados usando query params, ex: /api/products/?limit=2&offset=4

    @method_decorator(cache_page(60 * 60 * 2, key_prefix='product_list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_queryset(self):
        import time
        time.sleep(2)
        return super().get_queryset()

    def get_permissions(self):
        self.permission_classes = [AllowAny] 
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()

class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

    def get_permissions(self):
        self.permission_classes = [AllowAny] 
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            self.permission_classes = [IsAdminUser]
        return super().get_permissions()
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.prefetch_related('items__product')
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = None
    filterset_class = OrderFilter 
    filter_backends = [DjangoFilterBackend]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self): # type: ignore
        if self.action in ['create', 'update']:
            return OrderCreateSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
        return qs

    
class ProductInfoAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = None