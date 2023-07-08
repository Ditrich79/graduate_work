from django.shortcuts import render, get_object_or_404
from .models import Worlds


def worlds(request):
    worlds = Worlds.objects.all()
    return render(request, 'living_worlds/worlds.html', {'worlds': worlds})


def world(request, world_id):
    world = get_object_or_404(Worlds, pk=world_id)
    return render(request, 'living_worlds/world.html', {'world': world})
