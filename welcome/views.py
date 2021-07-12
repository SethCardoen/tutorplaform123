from django.shortcuts import render
from student.views import student_register_page
from stutor.views import register_page

def register(request):
    return render(request, 'welcome/home.html')

def about_view(request):
    return render(request, 'welcome/about.html')
