from django.urls import path
from . import views

urlpatterns = [
    path('initial/', views.members, name='initial'),
]