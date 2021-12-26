from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

from stutor.models import LessonRequest
from .models import student_account

class create_student_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class student_account_form(ModelForm):
    class Meta:
        model = student_account
        fields = '__all__'
        exclude = ['user']

class CreateNewLessonRequest_form(ModelForm):
    class Meta:
        model = LessonRequest
        fields = '__all__'
        exclude = ['student_account','status']
