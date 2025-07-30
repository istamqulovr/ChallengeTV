from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from django.contrib.auth import login as auth_login

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()

            gender = form.cleaned_data.get('gender')
            UserProfile.objects.create(user=user, gender=gender)

            auth_login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'users/registration.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


@login_required
def profile_view(request):
    profile_data = UserProfile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {"profile_data": profile_data})


def logout_view(request):
    logout(request)
    return redirect('profile')
