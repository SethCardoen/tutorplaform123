from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/', views.student_page),
    path('tutor/', views.tutor),

]