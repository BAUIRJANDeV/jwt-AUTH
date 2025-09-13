from rest_framework import serializers
from .models import CartItem
from products.models import Phone
from products.serialisers import PhoneSerializer


class CartItemSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['id', 'phone', 'quantity', 'total_price']

    def get_total_price(self, obj):
        return obj.total_price()


class AddCartItemSerializer(serializers.Serializer):
    phone_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1)
