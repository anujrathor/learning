from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit_profile, name='edit'),
]
