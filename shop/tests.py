from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Sweet

class AddSweetViewTest(TestCase):

    def test_add_sweet_view_post(self):
        # Arrange - POST form data
        data = {
            "name": "Gulab Jamun",
            "category": "Milk-Based",
            "price": 15,
            "quantity": 40
        }

        # Act - POST to the form view
        response = self.client.post(reverse('add_sweet'), data)

        # Assert - check if sweet is created and redirected
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        self.assertEqual(Sweet.objects.count(), 1)
        sweet = Sweet.objects.first()
        self.assertEqual(sweet.name, "Gulab Jamun")
        self.assertEqual(sweet.category, "Milk-Based")
        self.assertEqual(sweet.price, 15)
        self.assertEqual(sweet.quantity, 40)
