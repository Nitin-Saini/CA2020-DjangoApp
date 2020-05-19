from django.contrib import admin
from django.urls import path
from djangoapp_1 import views

urlpatterns = [
    path('', views.home )
]