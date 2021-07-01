from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', views.student_page, name='student'),
    path('tutor/<str:pk_tutor>/', views.tutor_page, name='tutor'),

    path('create_session/<str:pk_create_session>/', views.create_session, name = 'create_session'),
    path('update_session/<str:pk_update_session>/', views.update_session, name = 'update_session'),
    path('delete_session/<str:pk_delete_session>/', views.delete_session, name = 'delete_session'),
]