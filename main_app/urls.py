from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', views.login_user, name='login_user'),
    path('garage/', views.garage, name='garage'),

]