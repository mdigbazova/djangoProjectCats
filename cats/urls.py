from django.urls import path, re_path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^cats/', views.index),

]
