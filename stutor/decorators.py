from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group

def unauthenticated_user(views_func):  #functie uit de views
    def wrapper_func(request,*args, **kwargs):  #eerst deze functie, dan de andere
        if request.user.is_authenticated: #als hij ingelogd is --> homepage
            return redirect('home')
        else:
            return views_func(request, *args, **kwargs) # anders, ga naar de view functie

    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request,*args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name # group krijgt de waarde van de group waar de user in zit

            if group in allowed_roles:  #als de group toegang heeft --> render the view
                return view_func(request,*args, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')
        return wrapper_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('student')
      #  if group == 'tutor':
        #    return redirect('tutor')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to view this page')
    return wrapper_function