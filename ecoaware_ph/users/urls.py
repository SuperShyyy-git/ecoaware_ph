

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('admin/users/', views.user_list, name='user_list'),
    path('admin/users/<int:user_id>/edit/', views.user_edit, name='user_edit'), 
    path('admin/users/<int:user_id>/toggle/', views.toggle_user_status, name='toggle_user_status'),
    path('admin/users/<int:user_id>/delete/', views.delete_user, name='delete_user'),


    path('profile/<str:username>/', views.user_profile, name='user_profile'),

  
    path('access-denied/', views.access_denied, name='access_denied'),
]
