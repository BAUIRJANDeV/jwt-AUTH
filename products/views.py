from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Category,Phone
from .serialisers import CategorySerializer,PhoneSerializer,CategoryiSerializer
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


class PhoneSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        query=request.GET.get('q','')
        if not query:
            return Response({'data': [], 'status': status.HTTP_200_OK})

        phones=Phone.objects.filter(name__icontains=query)
        serializer=PhoneSerializer(phones,many=True)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})

class CategoryList(APIView):
    def get(self,request):
        cateogry=Category.objects.all()
        serializer=CategoryiSerializer(cateogry,many=True)
        return Response({'data':serializer.data,'status':status.HTTP_200_OK})

class CategoryDetail(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({'msg': 'Bunday Categorya topilmadi!', 'status': status.HTTP_404_NOT_FOUND})

        serializer = CategoryiSerializer(category)
        return Response({'data': serializer.data, 'status': status.HTTP_200_OK})
