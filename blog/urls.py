from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post_detail, name='post_detail'),
    path('search/', views.post_search, name='post_search'),
    path('about/', views.about, name='about'),
]