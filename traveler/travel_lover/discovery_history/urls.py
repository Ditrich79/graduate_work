from django.urls import path
from . import views


urlpatterns = [
    path('discovery_history/', views.stories, name='discovery_history'),
    path('<int:story_id>/', views.story, name='story'),
]