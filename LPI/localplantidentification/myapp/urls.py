from django.urls import path
from django.contrib.auth import logout
from . import views

urlpatterns =[
    path("login/",views.index, name="index"),
    path("home/",views.home, name="home"),
    path("notifications/",views.notifications, name="notifications"),
    path("settings/",views.settings, name="settings"),
    path("upload/",views.upload, name="upload"),
    path("createaccount/",views.createaccount, name="createaccount"),
    path("forgot-password/",views.forgotpassword, name="forgotpassword"),
    path("plantcommunity/",views.plantcommunity, name="plantcommunity"),
    path("result/",views.result, name="result"),
    path("profile/",views.profile, name="profile"),
    path("logout/", views.custom_logout, name="logout"),
    path("acccreated/",views.acccreated, name="acccreated"),
   
    
]