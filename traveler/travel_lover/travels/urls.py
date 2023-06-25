from django.urls import path
from . import views


urlpatterns = [
    path('', views.travels, name='travels'),
]
