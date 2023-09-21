from django.test import TestCase
from django.test import Client
from restaurant.models import Menu


class MenuItemTestCase(TestCase):

    def setUp(self) -> None:
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="HotChocolate", price=75, inventory=100)
        
    def test_get_item_from_api(self):
        c = Client()
        response = c.get("http://localhost:8000/api/menu-items/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)