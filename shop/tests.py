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

class DeleteSweetViewTest(TestCase):
    def setUp(self):
        self.sweet = Sweet.objects.create(
            name="Gulab Jamun",
            category="Milk-Based",
            price=10,
            quantity=50
        )

    def test_delete_sweet(self):
        sweet_id = self.sweet.id
        response = self.client.post(reverse('delete_sweet', args=[sweet_id]))

        # Check redirect
        self.assertEqual(response.status_code, 302)

        # Check sweet is deleted
        self.assertFalse(Sweet.objects.filter(id=sweet_id).exists())

class SearchSortSweetViewTest(TestCase):
    def setUp(self):
        Sweet.objects.create(name="Kaju Katli", category="Nut-Based", price=50, quantity=10)
        Sweet.objects.create(name="Gulab Jamun", category="Milk-Based", price=30, quantity=20)
        Sweet.objects.create(name="Lollipop", category="Candy", price=5, quantity=100)

    def test_search_by_name(self):
        response = self.client.get(reverse('add_sweet'), {'search': 'Kaju'})
        self.assertContains(response, "Kaju Katli")
        self.assertNotContains(response, "Gulab Jamun")

    def test_search_by_category(self):
        response = self.client.get(reverse('add_sweet'), {'category': 'Milk-Based'})
        self.assertContains(response, "Gulab Jamun")
        self.assertNotContains(response, "Kaju Katli")

    def test_search_by_price_range(self):
        response = self.client.get(reverse('add_sweet'), {'min_price': 10, 'max_price': 40})
        self.assertContains(response, "Gulab Jamun")
        self.assertNotContains(response, "Kaju Katli")

    def test_sort_by_price(self):
        response = self.client.get(reverse('add_sweet'), {'sort': 'price'})
        sweets = list(response.context['sweets'])
        self.assertEqual(sweets[0].name, "Lollipop")
        self.assertEqual(sweets[-1].name, "Kaju Katli")

class PurchaseSweetViewTest(TestCase):
    def setUp(self):
        self.sweet = Sweet.objects.create(
            name="Gulab Jamun",
            category="Milk-Based",
            price=10,
            quantity=50
        )

    def test_purchase_success(self):
        response = self.client.post(reverse('purchase_sweet'), {
            'sweet_id': self.sweet.id,
            'quantity': 10
        })

        self.assertEqual(response.status_code, 302)
        self.sweet.refresh_from_db()
        self.assertEqual(self.sweet.quantity, 40)

    def test_purchase_insufficient_stock(self):
        response = self.client.post(reverse('purchase_sweet'), {
            'sweet_id': self.sweet.id,
            'quantity': 100
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Not enough stock")
        self.sweet.refresh_from_db()
        self.assertEqual(self.sweet.quantity, 50)
