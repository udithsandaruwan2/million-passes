from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerUser, name='register'),
    path('adminn-panel/', views.adminPanel, name='admin'),

    # path('users/', views.profiles, name='profiles'),
    # path('profile/<str:pk>/', views.userProfile, name='user-profile'),
    # path('user/account/', views.userAccount, name='account'),
    # path('user/analytics/', views.userAnalytics, name='analytics'),
    
    # path('user/update-profile/', views.updateProfile, name='update-profile'),
    
]