from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('getlogin/', views.getlogin, name='getlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('add_turf/', views.add_turf, name='add_turf'),
    path('getturf/', views.getturf, name='getturf'),
    path('view_turf/', views.view_turf, name='view_turf'),
    path('editturf/<int:id>/', views.editturf, name='editturf'),
    path('updateturf/<int:id>/', views.updateturf, name='updateturf'),
    path('deleteturf/<int:id>/', views.deleteturf, name='deleteturf'),
    path('add_category/', views.add_category, name='add_category'),
    path('getcat/', views.getcat, name='getcat'),
    path('view_category/', views.view_category, name='view_category'),
    path('editcat/<int:id>/', views.editcat, name='editcat'),
    path('updatecat/<int:id>/', views.updatecat, name='updatecat'),
    path('deletecat/<int:id>/', views.deletecat, name='deletecat'),
    path('add_manager/', views.add_manager, name='add_manager'),
    path('getmgr/', views.getmgr, name='getmgr'),
    path('view_manager/', views.view_manager, name='view_manager'),
    path('editmgr/<int:id>/', views.editmgr, name='editmgr'),
    path('updatemgr/<int:id>/', views.updatemgr, name='updatemgr'),
    path('deletemgr/<int:id>/', views.deletemgr, name='deletemgr'),
    path('view_contact/', views.view_contact, name='view_contact'),
]