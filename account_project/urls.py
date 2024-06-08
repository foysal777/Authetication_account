
from django.contrib import admin
from django.urls import path,include
from account_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'homepage'),
    path('account_app/' ,include('account_app.urls'))
]
