from django.shortcuts import render, get_object_or_404
from .models import Travels


def travels(request):
    travels = Travels.objects.all()
    return render(request, 'travels/travels.html', {'travels': travels})


def travel(request, travel_id):
    travel = get_object_or_404(Travels, pk=travel_id)
    return render(request, 'travels/travel.html', {'travel': travel})

