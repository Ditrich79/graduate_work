from django.shortcuts import render, get_object_or_404
from .models import Travels
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def travels(request):
    travels = Travels.objects.all()

    # page = request.GET.get('page')
    # results = 3
    # paginator = Paginator(travels, results)
    #
    # try:
    #     travels = paginator.page(page)
    # except PageNotAnInteger:
    #     page = 1
    #     travels = paginator.page(page)
    # except EmptyPage:
    #     page = paginator.num_pages
    #     travels = paginator.page(page)
    #
    # context = {
    #     {'travels': travels},
    #     {'paginator': paginator},
    # }

    return render(request, 'travels/travels.html', {'travels': travels})


def travel(request, travel_id):
    travel = get_object_or_404(Travels, pk=travel_id)
    return render(request, 'travels/travel.html', {'travel': travel})

