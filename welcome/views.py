from django.shortcuts import render

def register(request):
    return render(request, 'welcome/home.html')

def about_view(request):
    return render(request, 'welcome/about.html')
