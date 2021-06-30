from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('student/', views.student_page, name="student"),
    path('tutor/<str:pk_tutor>/', views.tutor_page, name="tutor"),

]