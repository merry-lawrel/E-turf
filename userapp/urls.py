from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('getreg/', views.getreg, name='getreg'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('memberlogin/', views.memberlogin, name='memberlogin'),
    path('turf/<int:id>/', views.turf, name='turf'),
    path('getbooking/', views.getbooking, name='getbooking'),
    path('viewbooking/', views.viewbooking, name='viewbooking'),
    path('getbill/', views.getbill, name='getbill'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('getc/', views.getc, name='getc'),
    #path('deletebooking/', views.deletebooking, name='deletebooking'),
]