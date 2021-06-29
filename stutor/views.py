from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    stu = student.objects.all()
  #  tut = tutor.objects.all()

  #  all = {'stu': stu, 'tut': tut}

    return render(request, 'stutor/dashboard.html', {'stu': stu})

def student_page(request):
    stu = student.objects.all()
    return render(request, 'stutor/students.html', {'stu': stu})

def tutor_page(request):
   # tut = tutor.objects.all()
    return render(request, 'stutor/tutor.html')
