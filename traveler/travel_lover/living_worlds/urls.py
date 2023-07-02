from django.urls import path
from . import views


urlpatterns = [
    path('living_worlds/', views.worlds, name='living_worlds'),
]

