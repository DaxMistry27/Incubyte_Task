from django.db import models

# Create your models here.
from django.db import models

class Sweet(models.Model):
    CATEGORY_CHOICES = [
        ("Chocolate", "Chocolate"),
        ("Candy", "Candy"),
        ("Pastry", "Pastry"),
        ("Nut-Based", "Nut-Based"),
        ("Milk-Based", "Milk-Based"),
        ("Vegetable-Based", "Vegetable-Based"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
