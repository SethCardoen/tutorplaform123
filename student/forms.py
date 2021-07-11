from django.forms import ModelForm
from stutor.models import session
from .models import student_account
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class create_student_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
