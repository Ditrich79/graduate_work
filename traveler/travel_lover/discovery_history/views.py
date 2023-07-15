from django.shortcuts import render, get_object_or_404
from .models import Stories


def stories(request):
    stories = Stories.objects.all()
    return render(request, 'discovery_history/stories.html', {'stories': stories})


def story(request, story_id):
    story = get_object_or_404(Stories, pk=story_id)
    return render(request, 'discovery_history/story.html', {'story': story})

