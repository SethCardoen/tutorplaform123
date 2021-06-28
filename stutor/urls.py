from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/', views.student),
    path('tutor/', views.tutor),

]