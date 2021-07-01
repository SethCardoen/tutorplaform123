from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    ses = session.objects.all()
    tut = tutor.objects.all()
    stu = student.objects.all()

    total_tutors = tut.count()
    total_students = stu.count()
    total_sessions = ses.count()
   # total_math = session.filter(subject='mathematics').count()

    return render(request, 'stutor/dashboard.html', {'ses': ses, 'tut': tut, 'stu': stu, 'total_tutors': total_tutors, 'total_students': total_students, 'total_sessions': total_sessions})
    return render(request, 'stutor/status.html', {'ses': ses, 'tut': tut, 'stu': stu, 'total_tutors': total_tutors, 'total_students': total_students,'total_sessions': total_sessions})

def student_page(request):
    stu = student.objects.all()
    return render(request, 'stutor/students.html', {'stu': stu})

def tutor_page(request, pk_tutor):
    tuto_spe = tutor.objects.get(id=pk_tutor)

    email = tuto_spe.email #atribute opvragen van de classe zelf
    phone = tuto_spe.phone_number
    bac = tuto_spe.bank_account
    #edlev = tuto_spe.subject.all() #van child naar parent

    session = tuto_spe.session_set.all()
    ses_count = session.count()

    all = {
        'tuto_spe': tuto_spe,
        'email': email,
        'phone': phone,
        'bac': bac,
        'session': session,
        'ses_count': ses_count,
    }

    return render(request, 'stutor/tutor.html', all)

def create_session(request):

    context = {}

    return render(request, 'stutor/session_form.html', context)

