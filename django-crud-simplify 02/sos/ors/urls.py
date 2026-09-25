from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.welcome),
    path('',views.welcome),
    path('signin/',views.user_signin),
    path('signup/',views.user_signup),
    path('logout/',views    .user_logout),
    path('list/',views.user_list),
    path('delete/<int:id>/', views.delete_user),
    path('save/',views.user_save),
    path('save/<int:id>/', views.user_save),
    # path('edit/<int:id>/', views.edit_user),
    # path('testlist/',views.test_list),
    # path('create/', views.create_session),
    # path('access/', views.access_session),
    # path('destroy/', views.destroy_session),
    # path('set/', views.set_cookies),
    # path('get/', views.get_cookies)
]


