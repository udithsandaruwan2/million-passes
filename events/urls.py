from django.urls import path
from . import views

urlpatterns = [
    path('blank/', views.blankPage, name="blank"),
    path('', views.eventsPage, name="events"),
    path('about/', views.aboutPage, name="about"),
]