from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'stutor/dashboard.html')

def student(request):
    return render(request, 'stutor/students.html')

def tutor(request):
    return render(request, 'stutor/tutor.html')
