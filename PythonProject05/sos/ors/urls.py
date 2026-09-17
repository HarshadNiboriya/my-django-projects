from django.urls import path
from . import views, admin
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome),
    path('', views.welcome),
    path('signup/', views.sign_up),
    path('signin/', views.sign_in),

]
