from django.urls import path
from .views import add_sweet, delete_sweet, purchase_sweet, restock_sweet

urlpatterns = [
    path('add/', add_sweet, name='add_sweet'),
    path('delete/<int:sweet_id>/', delete_sweet, name='delete_sweet'),
    path('purchase/', purchase_sweet, name='purchase_sweet'),
    path('restock/', restock_sweet, name='restock_sweet')
]

