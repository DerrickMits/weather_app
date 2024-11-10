from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.get_weather, name='get_weather'),
]
