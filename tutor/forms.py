from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

import stutor.models
from .models import tutor_account

class create_tutor_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class tutor_account_form(ModelForm):
    class Meta:
        model = tutor_account
        fields = '__all__'
        exclude = ['user']


