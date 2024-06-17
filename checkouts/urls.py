from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<str:pk>/', views.checkoutPage, name="checkout"),
    path('multi-checkout/<str:pk>/', views.multiCheckoutPage, name="multi-checkout"),
    
    path('payment/<str:pk>/', views.paymentPage, name="payment"),
    path('order-success/<str:pk>/', views.orderSuccessPage, name="order-success-massage"),
]
