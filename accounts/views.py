from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model



def signup(request):
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('')

    else:
        form = CustomUserCreationForm()
    context = {'form': form, }
    return render(request, 'accounts/signup.html', context)        


def signin(request):
    if request.user.is_authenticated:
        return redirect('')

    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('')

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'accounts/signin.html', context)


def signout(request):
    auth_logout(request)
    return redirect('')


def user_index(request):
    User = get_user_model()
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'accounts/user_index.html', context)