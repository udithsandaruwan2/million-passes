from django.urls import path
from . import views

urlpatterns = [
    path('scan/', views.scan_view, name='scan_view'),
    path('scan_checking.../', views.qr_code_handler, name='qr_code_handler'),
    path('scan-success/', views.scan_success, name='scan_success'),
    path('scan-failed/', views.failurePage, name='scan-failed'),
]
