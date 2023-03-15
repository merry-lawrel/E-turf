from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('mgrpage/', views.mgrpage, name='mgrpage'),
    path('mgrlogin/', views.mgrlogin, name='mgrlogin'),
    path('mgrlogout/', views.mgrlogout, name='mgrlogout'),
    path('mgrgetlogin/', views.mgrgetlogin, name='mgrgetlogin'),
    path('mgrviewbooking/', views.mgrviewbooking, name='mgrviewbooking'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('decline/<int:id>', views.decline, name='decline'),
]