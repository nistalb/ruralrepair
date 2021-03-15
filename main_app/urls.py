from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register_user, name='register_user'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('profile/delete', views.profile_delete, name='profile_delete'),
    path('garage/', views.garage, name='garage'),
    path('equipment/create', views.equipment_create, name='equipment_create'),
    path('equipment/<int:equipment_id>/show', views.equipment_show, name='equipment_show'),
    path('equipment/<int:equipment_id>/edit', views.equipment_edit, name='equipment_edit'),
    path('tool/index', views.tool_index, name='tool_index'),
    path('tool/create', views.tool_create, name='tool_create'),
    path('tool/<int:tool_id>/edit', views.tool_edit, name='tool_edit'),
    path('tool/<int:tool_id>/delete', views.tool_delete, name='tool_delete'),

]