from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.tutor_register_page, name="tutor_register"),
    path('login/', views.student_login_page, name="tutor_login"),
    path('logout/', views.logout_user, name="logout"),
    path('mystudents/', views.mystudents, name='mystudents'),
    path('findnewstudents/', views.findnewstudents, name='findnewstudents'),
    path('plannewlessons/', views.plannewlessons, name='plannewlessons'),
    path('viewpreviouslessons/', views.viewpreviouslessons, name='viewpreviouslessons'),
    path('stats/', views.stats, name='stats'),
    path('notes/', views.notes, name='notes'),
    path('videos/', views.videos, name='videos'),


]

app_name = "tutor"
