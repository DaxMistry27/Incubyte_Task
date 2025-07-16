from django.urls import path
from .views import add_sweet

urlpatterns = [
    path('add/', add_sweet, name='add_sweet'),
]
