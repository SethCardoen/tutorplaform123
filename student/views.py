from django.shortcuts import render, redirect
from .models import *
from .forms import create_student_form
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
            )

            messages.success(request, 'Student account was created for ' + username)
            return redirect('student_login')
    context = {'form': form}
    return render(request, 'student/registerpage.html', context)

@unauthenticated_user
def student_login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,  password=password)

        if user is not None:
            login(request, user)
            return redirect('student_home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'student/loginpage.html', context)

@login_required(login_url='student_login')
def student_dashboard(request):
    return render(request, 'student/dashboard.html')