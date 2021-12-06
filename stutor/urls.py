from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.stutor_login_page, name="stutor_login"),
    path('user/', views.user_page, name='user'),
    path('student/', views.student_page, name='student'),
    path('tutor/<str:pk_tutor>/', views.tutor_page, name='tutor'),
    path('newdashboard/', views.new_dashboard),
    path('logout/', views.logout_user, name="logout"),

    path('create_session/<str:pk_create_session>/', views.create_session, name = 'create_session'),
    path('update_session/<str:pk_update_session>/', views.update_session, name = 'update_session'),
    path('delete_session/<str:pk_delete_session>/', views.delete_session, name = 'delete_session'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="stutor/password_reset.html"), name="reset_password"), #deze zijn allemaal door django gemaakt, je kan ze aanpassen
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="stutor/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="stutor/password_reset_form.html"), name="password_reset_confirm"), # uidb64 wil zeggen encrypted in base 64, token makes sure the password is valid
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="stutor/password_reset_done.html"), name="password_reset_complete"),

    path('test/', views.test)
]
app_name = "stutor"
