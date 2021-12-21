from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.tutor_home, name='tutor_home'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.tutor_register_page, name="tutor_register"),
    path('mystudents/', views.mystudents, name='mystudents'),
    path('findnewstudents/', views.findnewstudents, name='findnewstudents'),
    path('plannewlessons/', views.plannewlessons, name='plannewlessons'),
    path('viewpreviouslessons/', views.viewpreviouslessons, name='viewpreviouslessons'),
    path('viewavailability', views.viewavailability, name='viewavailability'),
    path('enteravailability', views.enteravailability, name='enteravailability'),
    path('stats/', views.stats, name='stats'),
    path('notes/', views.notes, name='notes'),
    path('videos/', views.videos, name='videos'),
    path('logout/', views.logout, name='logout'),
]

app_name = "tutor"
