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
        #fields = '__all__'
        fields = ('date','subject','education_level','lessonformat','number_lessons','remarks','status')
        #exclude = ['student_account','status']
        labels  = {
            'date':'',
            'subject':'',
            'education_level':'',
            'lessonformat':'',
            'number_lessons':'',
            'remarks':'',
            'status':''
        }



        widgets = {
           # 'date': forms.DateInput(attrs={'class':'form-control'}),
           # 'subject': forms.TextInput(attrs={'class':'form-control'}),
           # 'education_level':forms.TextInput(attrs={'class':'form-control'}),
            'number_lessons':forms.TextInput(attrs={'class':'form-control','placeholder':'Number of lessons'}),
            'remarks':forms.TextInput(attrs={'class':'form-control','placeholder':'Remarks'}),
          #  'status':forms.TextInput(attrs={'class':'form-control'}),
        }