# -*- coding: utf-8 -*-
from django.urls import path
from app import views


urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
