from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('register/', views.tutor_register_page, name="tutor_register"),
    path('login/', views.student_login_page, name="tutor_login"),
    path('logout/', views.logout_user, name="logout"),


]

app_name = "tutor"
