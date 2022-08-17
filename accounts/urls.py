from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.login),
    path('signup' , views.signup),
    path('authenticate' , views.Authenticate),
    path('register' , views.register_account),
    path('logout' ,  views.logout)
]