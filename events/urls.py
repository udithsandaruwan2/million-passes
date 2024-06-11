from django.urls import path
from . import views

urlpatterns = [
    path('blank/', views.blankPage, name="blank"),
    path('', views.eventsPage, name="events"),
    path('about/', views.aboutPage, name="about"),
    path('event/<str:pk>/', views.singleEvent, name="single-event"),
    path('add-event/', views.addEvent, name="add-event"),
    path('update-event/<str:pk>/', views.updateEvent, name="update-event"),
    path('delete-event/<str:pk>/', views.deleteEvent, name="delete-event"),
    path('tickets/', views.ticketPage, name="tickets"),
    path('add-tickets/', views.addTicket, name="add-ticket"),
    # path('update-event/<str:pk>/', views.updateTicket, name="update-ticket"),
    path('delete-ticket/<str:pk>/', views.deleteTicket, name="delete-ticket"),
]