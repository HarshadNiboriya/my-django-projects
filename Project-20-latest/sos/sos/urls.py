from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test_sos),
    path('', include('ors.urls')),
    path('ors/', include('ors.urls')),
]