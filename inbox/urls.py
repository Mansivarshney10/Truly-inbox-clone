from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('welcome/<str:email>/', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('report/', views.report, name='report'),
    path('reset-password/', views.resetPassword, name='/reset-password'),
    path('', views.index, name='index'),
]
