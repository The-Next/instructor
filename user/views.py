from django.shortcuts import render, redirect
from django.contrib import auth # authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import LoginForm, RegForm

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request, 'user/login.html', context)

def logout(request):
    # referer = request.META.get('HTTP_REFERER', reverse('index'))
    auth.logout(request)
    return redirect(request.GET.get('from', reverse('index')))

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)
            user.save()

            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('index')))
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request, 'user/register.html', context)

def profile(request):
    context = {}
    return render(request, 'user/profile.html', context)
