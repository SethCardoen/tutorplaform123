from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('user/', views.user_page, name='user_page'),
    path('student/', views.student_page, name='student'),
    path('tutor/<str:pk_tutor>/', views.tutor_page, name='tutor'),

    path('create_session/<str:pk_create_session>/', views.create_session, name = 'create_session'),
    path('update_session/<str:pk_update_session>/', views.update_session, name = 'update_session'),
    path('delete_session/<str:pk_delete_session>/', views.delete_session, name = 'delete_session'),
]