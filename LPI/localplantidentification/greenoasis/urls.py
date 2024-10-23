from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.index, name='index'),
    path("createaccount/",views.createaccount, name="createaccount"),
    path("forgot-password/",views.forgotpassword, name="forgotpassword"),
    path("acccreated/",views.acccreated, name="acccreated"),
    path("invalid-message/",views.invalidmessage, name="invalidmessage"),
    path("userexist/",views.userexist, name="userexist"),
    path("home/",views.home, name="home"),
    path('<int:id>/', views.detail_view, name='detail_view'),
    path('search/', views.search, name='search'),
    path("upload/",views.upload, name="upload"),
    path('edit/', views.editpost, name='editpost'),
    path('<int:id>/edit/', views.editpost, name='editpost'),
    path('<int:id>/delete/', views.deletepost, name='deletepost'),
  
    path("logout/", views.custom_logout, name="logout"),
]
