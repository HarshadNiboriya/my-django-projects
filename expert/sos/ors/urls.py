from django.contrib import admin
from django.urls import path
from . import views_latest

urlpatterns = [
    path('', views_latest.welcome),
    path('logout/', views_latest.user_logout),
    path('<page>/', views_latest.action),
    path('<page>/<operation>/<int:id>/', views_latest   .action),
]