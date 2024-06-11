from django.urls import path
from . import views

urlpatterns = [
    path('checkout/<str:pk>', views.checkoutPage, name="checkout"),
]