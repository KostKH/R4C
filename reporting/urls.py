from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('production-report/<int:year>/<int:week>/', views.production_report,
         name='production_report'),
]
