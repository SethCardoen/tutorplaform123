from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='home_register'),
    path('/about', views.about_view, name='about'),
]