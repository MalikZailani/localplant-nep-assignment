from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.index, name='index'),
    path("createaccount/",views.createaccount, name="createaccount"),
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
    path('passwordchange/', views.passwordchange, name='passwordchange'),
    path('passwordchangedone/', views.passwordchangedone, name='passwordchangedone'),

     path('password_reset/', 
         auth_views.PasswordResetView.as_view(template_name='passwordreset.html'), 
         name='password_reset'),
    path('passwordreset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='passwordresetdone.html'), 
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='passwordresetconfirm.html'), 
         name='password_reset_confirm'),
    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'), 
         name='password_reset_complete'),

     path('like/<int:id>/', views.like_post, name='like_post'),

     path('feedback/', views.feedback_view, name='feedback'),
    
    path("logout/", views.custom_logout, name="logout"),
]
