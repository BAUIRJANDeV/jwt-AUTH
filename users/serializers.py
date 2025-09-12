from django.contrib.auth import aget_user
from django.contrib.auth import authenticate
from .models import CutomUser
from rest_framework import  serializers
from rest_framework.generics import GenericAPIView
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class  RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(required=True,max_length=12)
    password2=serializers.CharField(required=True,max_length=12)
    class Meta:
        model=CutomUser
        fields=['id','username','email','age','addres','password','password2']

    def validate(self, data):
        password=data.get('password',None)
        password2=data.get('password2',None)

        if password2 is None and password is None:
            raise ValidationError({'message':'Parol toliq kiritilmadi!'})

        if password!=password2:
            raise ValidationError({'message':'Parolar mos kelmadi'})
        return data
    def create(self, validated_data):
        user=CutomUser.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            email=validated_data.get('email'),
            age=validated_data.get('age'),
            addres=validated_data.get('addres')
        )
        return user

class LoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(write_only=True,max_length=12)

    def validate(self, data):
        email=data.get('email')
        password=data.get('password')

        if not email and not password:
            raise ValidationError({'msg':'Login yoki parolni toliq kirting!'})
        user=authenticate(email=email,password=password)
        if not user:
            raise ValidationError({'msg':'Login yoki parol notogri'})
        data['user']=user
        return data
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CutomUser
        fields = ['email', 'addres', 'age']


