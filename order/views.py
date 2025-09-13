from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .models import Order, OrderItem
from card.models import CartItem
from products.models import Phone
from .serializers import OrderSerializer


class CreateOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        if not cart_items.exists():
            return Response({"error": "Savatcha bo‘sh"}, status=400)

        order = Order.objects.create(user=request.user)

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                phone=item.phone,
                quantity=item.quantity
            )


        cart_items.delete()

        return Response({"message": "Buyurtma yaratildi", "order_id": order.id}, status=201)



class MyOrdersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)



class OrderDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        try:
            order = Order.objects.get(id=id, user=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Buyurtma topilmadi"}, status=404)

        serializer = OrderSerializer(order)
        return Response(serializer.data)



class CancelOrderView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id):
        try:
            order = Order.objects.get(id=id, user=request.user)
        except Order.DoesNotExist:
            return Response({"error": "Buyurtma topilmadi"}, status=404)

        if order.is_canceled:
            return Response({"message": "Buyurtma allaqachon bekor qilingan"})

        order.is_canceled = True
        order.save()

        return Response({"message": "Buyurtma bekor qilindi"})



