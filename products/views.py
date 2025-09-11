from django.shortcuts import render
from .models import Category,Phone
from .serialisers import CategorySerializer,PhoneSerializer
from rest_framework.views import APIView
from rest_framework import status,generics
from rest_framework.response import Response

class PhoneList(generics.ListAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneDetail(generics.RetrieveAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneCreate(generics.CreateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneDelete(generics.DestroyAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

class PhoneUpdate(generics.UpdateAPIView):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

# Create your views here.
