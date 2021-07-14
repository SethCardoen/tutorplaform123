from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.student_register_page, name='student_register'),
    path('home/', views.student_dashboard, name='student_home'),
    path('logout/', views.logout, name='logout'),
]

app_name = "student"