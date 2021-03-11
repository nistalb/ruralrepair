from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register_user, name='register_user'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('garage/', views.garage, name='garage'),

]