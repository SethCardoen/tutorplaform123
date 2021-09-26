from django.shortcuts import render, redirect
from .models import tutor_account
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from stutor.decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group
from .forms import create_tutor_form, tutor_account_form
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


@unauthenticated_user
def tutor_register_page(request):
    form = create_tutor_form()
    if request.method == 'POST':
        form = create_tutor_form(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            username = form.cleaned_data.get('username')

            user_group = Group.objects.get(name="tutor")
            user.groups.add(user_group)
            tutor_account.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('tutor:tutor_login')
    context = {'form': form}
    return render(request, 'tutor/registerpage.html', context)


@unauthenticated_user
def student_login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            users_in_group = Group.objects.get(name="tutor").user_set.all()
            if user in users_in_group:
                return redirect('tutor:home')
            else:
                return redirect('student:student_home')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'tutor/loginpage.html', context)


def logout_user(request):
    logout(request)
    return redirect('tutor:tutor_login')


def home(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'tutor'])
def settings(request):
    tutor = request.user.tutor_account
    print(tutor)
    form = tutor_account_form(instance=tutor)

    if request.method == 'POST':
        form = tutor_account_form(request.POST, request.FILES, instance=tutor)
        if form.is_valid():
            form.save()
            return redirect('tutor:home')

    context = {'form': form, 'tutor':tutor}
    return render(request, 'tutor/settings.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def mystudents(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/mystudents.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def findnewstudents(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/findnewstudents.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def plannewlessons(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/plannewlessons.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def viewpreviouslessons(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/viewpreviouslessons.html', context)
# 
@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def stats(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/stats.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def notes(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/notes.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['tutor'])
def videos(request):
    tutor = request.user.tutor_account
    context = {'tutor': tutor}
    return render(request, 'tutor/videos.html', context)
