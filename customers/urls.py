from django.urls import path
from . import views
urlpatterns = [
    
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/address/', views.AddressView.as_view(), name='profile'),
    
]

