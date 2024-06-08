
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'homepage'),
    path('register/', views.register, name= 'register'),
    path('log_in/', views.log_in, name= 'log_in'),
    path('log_out/', views.log_out, name= 'log_out'),
    path('profile/', views.profile, name= 'profile'),
    path('pass_change/', views.pass_change, name= 'pass_change'),
    path('pass_2/', views.pass_2, name= 'pass_2'),
   
    
    ]
   
