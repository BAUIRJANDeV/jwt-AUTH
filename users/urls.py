from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenBlacklistView
from django.urls import path
from .views import RegisterApi,test

urlpatterns=[
    path('regis/',RegisterApi.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    path('logout/',TokenBlacklistView.as_view()),
    path('test/',test),
]
