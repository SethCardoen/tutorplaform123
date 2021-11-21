from django.shortcuts import render, redirect

import stutor.models
import tutor
from stutor.models import *
from tutor.models import tutor_account

from .models import student_account
from .forms import create_student_form, student_account_form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stutor.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


@unauthenticated_user
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
            return redirect('tutor:tutor_login')
    context = {'form': form}
    return render(request, 'student/registerpage.html', context)

@login_required(login_url='tutor:tutor_login')
def student_dashboard(request):
    #teach = tutor_account.objects.all()
    student = request.user.student_account
    teach = request.user.student_account.linked_tutors.all()



   # teach = tutor_account.objects.get(id=pk_student)

   # tutor_sidebar_filter_them = tutor_sidebar_filter(request.GET, queryset=teach)
   # teachere = tutor_sidebar_filter_them.qs
    context ={'student': student, 'teachere': teach}
    return render(request, 'student/dashboard.html', context)

def logout(request):
    logout(request)
    return redirect('tutor:tutor_login')

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
def plannewlessons(request):
    student = request.user.student_account
    context = {'student': student}
    return render(request, 'student/plannewlessons.html', context)

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

