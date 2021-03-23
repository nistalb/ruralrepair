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
    path('equipment/<int:equipment_id>/delete', views.equipment_delete, name='equipment_delete'),
    path('equipment/<int:equipment_id>/add_photo', views.add_photo, name='add_photo'),
    path('equipment/<int:equipment_id>/<int:photo_id>/delete_photo', views.delete_photo, name='delete_photo'),
    path('tool/index', views.tool_index, name='tool_index'),
    path('tool/create', views.tool_create, name='tool_create'),
    path('tool/<int:tool_id>/edit', views.tool_edit, name='tool_edit'),
    path('tool/<int:tool_id>/delete', views.tool_delete, name='tool_delete'),
    path('consumable/index', views.consumable_index, name='consumable_index'),
    path('consumable/create', views.consumable_create, name='consumable_create'),
    path('consumable/<int:consumable_id>/edit', views.consumable_edit, name='consumable_edit'),
    path('consumable/<int:consumable_id>/delete', views.consumable_delete, name='consumable_delete'),
    path('task/<int:equipment_id>/create', views.task_create, name='task_create'),
    path('task/<int:task_id>/show', views.task_show, name='task_show'),
]