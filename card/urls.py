from django.urls import path
from .views import CartView, AddToCartView, UpdateCartView, RemoveFromCartView

urlpatterns = [
    path('api/cart/', CartView.as_view()),
    path('api/cart/add/', AddToCartView.as_view()),
    path('api/cart/update/', UpdateCartView.as_view()),
    path('api/cart/remove/<int:id>/', RemoveFromCartView.as_view()),
]
