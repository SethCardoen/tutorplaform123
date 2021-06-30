from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('student/', views.student_page),
    path('tutor/<str:pk_tutor>/', views.tutor_page),

]