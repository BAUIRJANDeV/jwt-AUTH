from django.urls import path
from .views import CreateOrderView, MyOrdersView, OrderDetailView, CancelOrderView

urlpatterns = [
    path('api/orders/create/', CreateOrderView.as_view()),
    path('api/orders/', MyOrdersView.as_view()),
    path('api/orders/<int:id>/', OrderDetailView.as_view()),
    path('api/orders/<int:id>/cancel/', CancelOrderView.as_view()),
]
