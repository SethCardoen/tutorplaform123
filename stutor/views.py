from django.shortcuts import render, redirect
from .models import *
from .forms import sessionform
from .filters import session_filter
#from django.forms import inlineformset_factory

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

    tutor_page_filter = session_filter(request.GET, queryset=session) #trow the data in the filter --> filter
    session = tutor_page_filter.qs # output the filtered data --> redefine it

    all = {
        'tuto_spe': tuto_spe,
        'email': email,
        'phone': phone,
        'bac': bac,
        'session': session,
        'ses_count': ses_count,
        'tutor_page_filter': tutor_page_filter,
    }

    return render(request, 'stutor/tutor.html', all)

def create_session(request, pk_create_session):
    #session_form_set = inlineformset_factory(tutor, session, fields=(fiel) #give it first the parent, than the child model
    tuto_spe = tutor.objects.get(id=pk_create_session)
    form = sessionform(initial={'tutor': tuto_spe, 'subject': tuto_spe.subject, 'price_an_hour': tuto_spe.price_an_hour})
    if request.method == 'POST':
        form = sessionform(request.POST) #if the method is post, than we return the request data from the form
        if form.is_valid():
            form.save()
            return redirect('/')

        #print('Printing POST:', request.POST)

    context = {'form': form}
    return render(request, 'stutor/session_form.html', context)

def update_session(request, pk_update_session):
    sessio = session.objects.get(id=pk_update_session)
    form = sessionform(instance=sessio)

    if request.method == 'POST':        #sending new post data from update to the form
        form = sessionform(request.POST, instance=sessio)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'stutor/session_form.html', context)

def delete_session(request, pk_delete_session):
    sessio = session.objects.get(id=pk_delete_session)

    if request.method == "POST":
        sessio.delete()
        return redirect('/')

    context = {'sessio': sessio}
    return render(request, 'stutor/delete.html', context)

