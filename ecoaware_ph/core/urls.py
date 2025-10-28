from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('my-campaigns/', views.my_campaigns, name='my_campaigns'),
    path('some-route/', views.some_view, name='some_route'),

]
