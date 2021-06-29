from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    ses = session.objects.all()
    tut = tutor.objects.all()
    stu = student.objects.all()

    total_tutors = tut.count()
    total_students = stu.count()
    total_sessions =  ses.count()
    # all math: total_math = session.filter('mathematics).count()

    return render(request, 'stutor/dashboard.html', {'ses': ses, 'tut': tut, 'stu': stu, 'total_tutors': total_tutors, 'total_students': total_students, 'total_sessions': total_sessions})
    return render(request, 'stutor/status.html', {'ses': ses, 'tut': tut, 'stu': stu, 'total_tutors': total_tutors, 'total_students': total_students,'total_sessions': total_sessions})

def student_page(request):
    stu = student.objects.all()
    return render(request, 'stutor/students.html', {'stu': stu})

def tutor_page(request):
   # tut = tutor.objects.all()
    return render(request, 'stutor/tutor.html')
