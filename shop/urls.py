from django.urls import path
from .views import add_sweet, delete_sweet

urlpatterns = [
    path('add/', add_sweet, name='add_sweet'),
    path('delete/<int:sweet_id>/', delete_sweet, name='delete_sweet'),
]
