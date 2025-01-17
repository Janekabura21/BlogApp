from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name='home'),  
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Login URL
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),  
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.register, name='register'),
]
