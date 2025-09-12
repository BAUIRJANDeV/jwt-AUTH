from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated

from .models import Category,Phone
from .serialisers import CategorySerializer,PhoneSerializer
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response

class PhoneList(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneDelete(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

# Create your views here.
