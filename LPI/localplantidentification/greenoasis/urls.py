from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

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
    path('profile', views.profile, name='profile'),
    path('editprofile', views.editprofile, name='editprofile'),
    path('setting/', views.settings, name='settings'),
    path('deleteprofile/', views.deleteprofile, name='deleteprofile'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='passwordchange.html'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    path("logout/", views.custom_logout, name="logout"),
]
