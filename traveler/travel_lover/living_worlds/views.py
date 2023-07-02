from django.shortcuts import render


def worlds(request):
    return render(request, 'living_worlds/living_worlds.html')
