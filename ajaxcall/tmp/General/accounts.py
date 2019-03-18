from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import auth_login
from django.contrib.auth import logout
from django.contrib.auth.models import User


from .models import TIME_MANAGEMENT ,EXCHANGE ,VOIP ,VIRTUAL_MACHINE 
from .forms import SignUpForm , TIME_MANAGEMENT_Form ,EXCHANGE_Form ,VOIP_Form ,VIRTUAL_MACHINE_Form 

from .json_import import PRICE_TABLE


@login_required(login_url='General:login')
def home(request):
    context = {}
    context.update({ 'time_management' : { 'item' : TIME_MANAGEMENT.objects.all() }})
    context.update({ 'exchange' : { 'item' : EXCHANGE.objects.all() }})
    context.update({ 'voip' : { 'item' : VOIP.objects.all() }})
    context.update({ 'virtual_machine' : { 'item' : VIRTUAL_MACHINE.objects.all() }})
    return render(request, 'General/Home.html' ,  context )


def signup(request):
    if request.user.is_authenticated:
        return redirect('General:home')
    if request.method == 'POST':
        SignUp = SignUpForm(request.POST)
        try:
            cache = request.session['saved']
        except KeyError:
            cache = {}
        if SignUp.is_valid():
            email = SignUp.cleaned_data.get('email')
            username = SignUp.cleaned_data.get('email')
            raw_password = SignUp.cleaned_data.get('password1')
            try:
                user = User.objects.create_user(username, email , raw_password)
                user.save()
                user = authenticate(username=username, password=raw_password)
                auth_login(request, user)
                current = request.user
                try:
                  time_management_form = TIME_MANAGEMENT_Form(cache,user=current)
                  if time_management_form.is_valid():
                    time_management_form.save()
                except Exception as e:
                  pass
                try:
                  exchange_form = EXCHANGE_Form(cache,user=current)
                  if exchange_form.is_valid():
                    exchange_form.save()
                except Exception as e:
                  pass
                try:
                  voip_form = VOIP_Form(cache,user=current)
                  if voip_form.is_valid():
                    voip_form.save()
                except Exception as e:
                  pass
                try:
                  virtual_machine_form = VIRTUAL_MACHINE_Form(cache,user=current)
                  if virtual_machine_form.is_valid():
                    virtual_machine_form.save()
                except Exception as e:
                  pass
            except IntegrityError:
                context = add_Menu_and_list(request)
                context.update({ 'form': SignUp })
                context.update({ 'Title': 'Sign up' , 'sigup_error' : 'User Already Exist' })
                return render(request, 'General/signup.html',  context )
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('General:home')
    else:
        SignUp = SignUpForm()
    context.update({ 'form': SignUp })
    context.update({ 'Title': 'Sign up' })
    return render(request, 'General/signup.html',  context )


def login(request):
    if request.user.is_authenticated:
        return redirect('General:home')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('General:home')
        else:
            context.update({ 'form' : login_form })
            return render(request, 'General/login.html', context)
    login_form = AuthenticationForm()
    context.update({ 'form' : login_form })
    return render(request, 'General/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('General:login')