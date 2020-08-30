from rest_framework import serializers
from .models import Product,OrderItem,Order


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'product_name', 'price')

class OrderItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product', 'quantity','price')

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'orderitem', 'order_status')
