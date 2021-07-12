from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.student_register_page, name='student_register'),
    path('login/', views.student_login_page, name='student_login'),
    path('home/', views.student_dashboard, name='student_home'),
    path('logout/', views.logout_user, name='logout'),
]