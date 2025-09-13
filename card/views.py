from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import CartItem
from products.models import Phone
from .serializers import CartItemSerializer, AddCartItemSerializer


class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        total_sum = sum([item.total_price() for item in cart_items])
        return Response({
            'items': serializer.data,
            'total_sum': total_sum
        })


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = AddCartItemSerializer(data=request.data)
        if serializer.is_valid():
            phone_id = serializer.validated_data['phone_id']
            quantity = serializer.validated_data['quantity']

            try:
                phone = Phone.objects.get(id=phone_id)
            except Phone.DoesNotExist:
                return Response({"error": "Telefon topilmadi"}, status=404)

            item, created = CartItem.objects.get_or_create(user=request.user, phone=phone)
            if not created:
                item.quantity += quantity
            else:
                item.quantity = quantity
            item.save()

            return Response({"message": "Mahsulot savatchaga qo‘shildi"}, status=201)
        return Response(serializer.errors, status=400)


class UpdateCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request):
        serializer = AddCartItemSerializer(data=request.data)
        if serializer.is_valid():
            phone_id = serializer.validated_data['phone_id']
            quantity = serializer.validated_data['quantity']

            try:
                item = CartItem.objects.get(user=request.user, phone_id=phone_id)
                item.quantity = quantity
                item.save()
                return Response({"message": "Miqdori yangilandi"})
            except CartItem.DoesNotExist:
                return Response({"error": "Mahsulot topilmadi"}, status=404)

        return Response(serializer.errors, status=400)


class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, id):
        try:
            item = CartItem.objects.get(id=id, user=request.user)
            item.delete()
            return Response({"message": "Mahsulot savatchadan o‘chirildi"})
        except CartItem.DoesNotExist:
            return Response({"error": "Topilmadi"}, status=404)


