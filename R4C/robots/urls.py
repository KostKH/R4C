from django.urls import path

from . import views

urlpatterns = [
    path('', views.new_robot, name='new_robot'),
]
