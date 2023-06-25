from django.shortcuts import render
from .models import Travels


def travels(request):
    travels = Travels.objects.all()
    return render(request, 'travels/travels.html', {'travels': travels})
