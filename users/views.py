from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import CutomUser
from .serializers import RegisterSerializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


class RegisterApi(GenericAPIView):
    queryset = CutomUser
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Siz royhatan otingiz",'status':status.HTTP_201_CREATED})
        return Response({'errors':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})

@api_view(['GET'])
# @permission_classes([AllowAny])
def test(request):
    return Response({'data':True})







