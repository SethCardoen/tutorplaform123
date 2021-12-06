from django.shortcuts import render, redirect
from .models import *
from .forms import sessionform, create_user_form
from .filters import session_filter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from student.models import student_account
from tutor.models import tutor_account
from tutor.forms import tutor_account_form
from django.contrib.auth.forms import UserCreationForm
#from django.forms import inlineformset_factory

def logout_user(request):
    logout(request)
    return redirect('stutor:stutor_login')

@unauthenticated_user
def stutor_login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            users_in_group = Group.objects.get(name="tutor").user_set.all()
            if user in users_in_group:
                return redirect('tutor:stutor_home')
            else:
                return redirect('student:student_home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'stutor/loginpage.html', context)

@login_required(login_url='login')
@admin_only
def home(request):
    ses = session.objects.all()
    tut = tutor_account.objects.all()
    stu = student_account.objects.all()


    total_tutors = tut.count()
    total_students = stu.count()
    total_sessions = ses.count()
   # total_math = session.filter(subject='mathematics').count()

    return render(request, 'stutor/student_home.html', {'ses': ses, 'tut': tut, 'stu': stu, 'total_tutors': total_tutors, 'total_students': total_students, 'total_sessions': total_sessions})
    return render(request, 'stutor/status.html', {'ses': ses, 'tut': tut, 'stu': stu, 'total_tutors': total_tutors, 'total_students': total_students,'total_sessions': total_sessions})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def student_page(request):
    stu = student_account.objects.all()
    return render(request, 'stutor/students.html', {'stu': stu})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'tutor'])
def tutor_page(request, pk_tutor):
    tuto_spe = tutor_account.objects.get(id=pk_tutor)

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


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def user_page(request):
    tuto_profile = tutor_account.objects.get(user=request.user)
    sessionn = tuto_profile.session_set.all()

    total_sessions = sessionn.count()

    context = {'sessionn': sessionn, 'total_sessions': total_sessions}
    return render(request, 'stutor/user.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_session(request, pk_create_session):
    #session_form_set = inlineformset_factory(tutor, session, fields=(fiel) #give it first the parent, than the child model
    tuto_spe = tutor_account.objects.get(id=pk_create_session)
    form = sessionform(initial={'tutor': tuto_spe, 'subject': tuto_spe.subject, 'price_an_hour': tuto_spe.price_an_hour})
    if request.method == 'POST':
        form = sessionform(request.POST) #if the method is post, than we return the request data from the form
        if form.is_valid():
            form.save()
            return redirect('/')

        #print('Printing POST:', request.POST)

    context = {'form': form}
    return render(request, 'stutor/session_form.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete_session(request, pk_delete_session):
    sessio = session.objects.get(id=pk_delete_session)

    if request.method == "POST":
        sessio.delete()
        return redirect('/')

    context = {'sessio': sessio}
    return render(request, 'stutor/delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def new_dashboard(request):
    return render(request, 'stutor/index.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def test(request):
    return render(request, 'static/css/test.html')




