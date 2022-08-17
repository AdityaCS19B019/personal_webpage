from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('skills' , views.skills) ,
    path('projects' , views.projects) ,
    path('experience' , views.experience) ,
    # path('register_page/' , views.register , name='register')
]