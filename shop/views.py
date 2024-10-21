from django.core.cache import cache
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        products = cache.get('product_list')
        if products is None:
            products = Product.objects.all()
            cache.set('product_list', products, timeout=60 * 15)
        return products

    def perform_create(self, serializer):
        serializer.save()
        cache.delete('product_list')

    def perform_update(self, serializer):
        serializer.save()
        cache.delete('product_list')

    def perform_destroy(self, instance):
        instance.delete()
        cache.delete('product_list')


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
