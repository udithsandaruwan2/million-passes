from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<str:pk>/', views.checkoutPage, name="checkout"),
    path('multi-checkout/<str:pk>/', views.multiCheckoutPage, name="multi-checkout"),
    
    path('payment/<str:pk>/', views.paymentPage, name="payment"),
    path('multi-payment/<str:pk>/', views.multiPaymentPage, name="multi-payment"),
    
    path('order-success/<str:pk>/', views.orderSuccessPage, name="order-success-massage"),
    # path('multi-order-success/<str:pk>/', views.multiOrderSuccessPage, name="multi-order-success-massage"),
    
    path('download-qr-codes/', views.download_qr_codes, name='download_qr_codes'),
    

]
