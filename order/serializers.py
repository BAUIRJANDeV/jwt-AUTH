from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Phone
from products.serialisers import PhoneSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'phone', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'is_canceled', 'items', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()
