from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class sessionform(ModelForm):
    class Meta:           #define which models, and which fields to use
        model = session
        fields = '__all__'  #otherwise ['date', 'time'] for only date and time

class create_user_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']