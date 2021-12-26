from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
import stutor.models
import tutor
from stutor.models import *
from tutor.models import tutor_account
from datetime import datetime

from .models import student_account
from .forms import create_student_form, student_account_form,CreateNewLessonRequest_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stutor.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

def student_register_page(request):

    form = create_student_form()
    if request.method == 'POST':
        form = create_student_form(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            username = form.cleaned_data.get('username')

            user_group = Group.objects.get(name="student")
            user.groups.add(user_group)
            student_account.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )

            messages.success(request, 'Student account was created for ' + username)
            return redirect('stutor:stutor_login')
    context = {'form': form}
    return render(request, 'student/registerpage.html', context)

@login_required(login_url='stutor:stutor_login')
def student_home(request):

    student = request.user.student_account
    teach = request.user.student_account.linked_tutors.all()
    context ={'student': student, 'teacher': teach}
    return render(request, 'student/student_home.html', context)


def logout(request):
    logout(request)
    return redirect("/")
    #return redirect('stutor:stutor_login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'student'])
def settings(request):
    student = request.user.student_account
    form = student_account_form(instance=student)

    if request.method == 'POST':
        form = student_account_form(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:student_home')

    context = {'form': form, 'student':student}
    return render(request, 'student/settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def mytutors(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/mytutors.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def findnewtutors(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/findnewtutors.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def mycalendar(request,year,month):
    # convert month to uppercase
    month = month.title()
    # convert month from str to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    # create calendar
    cal = HTMLCalendar().formatmonth(year, month_number)

    #get current date
    now = datetime.now()
    current_year = now.year
    #get current time
    time = now.strftime('%I:%M:%S')

    student = request.user.student_account
    context = {
                'student': student,
                'year':year,
                'month':month,
                'month_number':month_number,
                'cal':cal,
                'current_year':current_year,
                'time':time}

    return render(request, 'student/mycalendar.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def myrequests(request):

    student = request.user.student_account
    all_requests = LessonRequest.objects.all()
    my_requests = all_requests.filter(student_account=student)

    submitted = False
    if request.method == "POST":
        form = CreateNewLessonRequest_form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.student_account = student
            post.save()
            return HttpResponseRedirect('/student/plannewlessons/?submitted=True')
    else:
        form = CreateNewLessonRequest_form
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form, 'submitted':submitted, 'student':student,'my_requests':my_requests}
    return render(request, 'student/myrequests.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def tasks(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/tasks.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def viewpreviouslessons(request):
    student = request.user.student_account
    allsesions = session.objects.all()
    mysessions = allsesions.filter(student = student)
    context = {'student': student, 'mysessions': mysessions}
    return render(request, 'student/viewpreviouslessons.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def stats(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/stats.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def notes(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/notes.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['student'])
def videos(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/videos.html', context)

