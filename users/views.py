from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Challenge, UserProfile




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

            if not hasattr(user, 'userprofile'):
                UserProfile.objects.create(user=user, gender=gender)

            auth_login(request, user)
            return redirect('profile')
        else:
            print(form.errors)
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



@login_required
def join_challenge(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        challenge_id = data.get('id')

        try:
            challenge = Challenge.objects.get(id=challenge_id)
            profile, created = UserProfile.objects.get_or_create(user=request.user)
            profile.challenges.add(challenge)
            return JsonResponse({'success': True})
        except Challenge.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Challenge not found'})

    return JsonResponse({'success': False, 'error': 'Invalid request'})

