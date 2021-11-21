from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.student_register_page, name='student_register'),
    path('home/', views.student_dashboard, name='student_home'),
    path('logout/', views.logout, name='logout'),
    path('settings/', views.settings, name='settings'),
    path('mytutors/', views.mytutors, name='mytutors'),
    path('findnewtutors/', views.findnewtutors, name='findnewtutors'),
    path('plannewlessons/', views.plannewlessons, name='plannewlessons'),
    path('tasks/', views.tasks, name='tasks'),
    path('viewpreviouslessons/', views.viewpreviouslessons, name='viewpreviouslessons'),
    path('stats/', views.stats, name='stats'),
    path('notes/', views.notes, name='notes'),
    path('videos/', views.videos, name='videos'),
]

app_name = "student"