from django.urls import path

from .views import PhoneList,PhoneCreate,PhoneDelete,PhoneDetail,PhoneUpdate

urlpatterns=[
    path('',PhoneList.as_view()),
    path('phone/<int:pk>/',PhoneDetail.as_view()),
    path('phone/update/<int:pk>/', PhoneUpdate.as_view()),
    path('phone/create/',PhoneCreate.as_view()),
    path('phone/delete/<int:pk>/',PhoneDelete.as_view())

]