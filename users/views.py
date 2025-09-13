from django.core.serializers import get_serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import CutomUser
from .serializers import RegisterSerializers,LoginSerializer,ProfileSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterApi(GenericAPIView):
    queryset = CutomUser  # Ehtimol: CustomUser bo‘lishi kerak
    serializer_class = RegisterSerializers
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Token yaratish
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response({
                'msg': "Siz ro‘yxatdan o‘tdingiz",
                'refresh': str(refresh),
                'access': str(access),
                'status': status.HTTP_201_CREATED
            })

        return Response({
            'errors': serializer.errors,
            'status': status.HTTP_400_BAD_REQUEST
        })




class LoginApi(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            token=RefreshToken.for_user(user)
            refresh=str(token)
            access=str(token.access_token)
            data={
                'refresh':refresh,
                'access':access,
                'status':status.HTTP_200_OK
            }
            return Response(data)
        return Response({"errors":serializer.errors,'status':status.HTTP_400_BAD_REQUEST})

class LogoutApi(APIView):
    def post(self,request):
        data=request.data
        try:
            token=RefreshToken(data['refresh'])
            token.blacklist()
            return Response({'msg':'Tizimdan chiqdingiz!'})
        except Exception as e:
            return Response({'errors':e,'staus':status.HTTP_400_BAD_REQUEST})


class TokenRefresh(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        data=request.data
        try:
            token=RefreshToken(data['refresh'])
            return Response({'access':str(token.access_token),'status':status.HTTP_200_OK})
        except Exception as e:
            return Response({'errors':e,'staus':status.HTTP_400_BAD_REQUEST})


class Profile(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serializer=ProfileSerializer(request.user)
        return Response({'data':serializer.data})

    def put(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=False)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data, 'status': status.HTTP_200_OK})
        return Response({'errors': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self,request):
        serializer=ProfileSerializer(request.user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()

            return Response({'data':serializer.data,'status':status.HTTP_200_OK})
        return Response({'errors':serializer.errors,'status':status.HTTP_400_BAD_REQUEST})
