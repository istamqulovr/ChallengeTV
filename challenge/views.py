from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Challenge


def index(request):
    return render(request,'challenge/home.html')


def challenge_tv(request):
    data = Challenge.objects.all()
    return render(request, 'challenge/index.html',{"data":data})


def workout(request, slug):
    challenge = get_object_or_404(Challenge, slug=slug)
    return render(request, 'challenge/workout.html', {'challenge': challenge})


@csrf_exempt
def update_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            challenge_id = data.get('id')
            new_status = data.get('status')

            challenge = Challenge.objects.get(id=challenge_id)

            if new_status in dict(Challenge.CHANGE_STATUS):
                challenge.status = new_status
                challenge.save()
                return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False})
