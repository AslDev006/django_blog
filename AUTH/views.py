from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from AUTH.forms import *
from AUTH.models import User, male, female
from django.shortcuts import render, redirect, get_object_or_404
import random
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect




def SignupPageView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            return redirect('signup2_page', user.id)
    else:
        form = SignupForm()
    return render(request, 'AUTH/signup.html', {"form": form})

def Signup2PageView(request, id):
    user = get_object_or_404(User,  id=id)
    user_form = SignUpPage2Form(request.POST, request.FILES, instance=user)
    if user_form.is_valid():
            user_form.save()
            print(user_form)
            return redirect('profile_page', user.id)
    context = {
        "male": male,
        "female": female,
        "form": user_form,
    }
    return render(request, 'AUTH/edit_profile.html', context)

def ProfilePage(request, id):
    user = get_object_or_404(User,  id=id)
    context = {
        "user": user,
        "male": male,
        "female": female,
    }
    return render(request, 'Auth/profile.html', context)

def LoginPageView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successfully !!!')
            return redirect('home_page')
        else:
            messages.success(request, 'There was an error logging in , try again....')
            return redirect('login_page')
    return render(request, 'AUTH/login.html', {})

def LogoutPageView(request):
    logout(request)
    messages.success(request, 'You were logged out !!!')
    return redirect('home_page')






def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'AUTH/change_password.html', {
        'form': form
    })