from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Challenge


def index(request):
    return render(request,'challenge/home.html')


def challenge_tv(request):
    data = Challenge.objects.all()
    return render(request, 'challenge/index.html',{"data":data})


def workout(request, slug):
    challenge = get_object_or_404(Challenge, slug=slug)
    return render(request, 'challenge/workout.html', {'challenge': challenge})
