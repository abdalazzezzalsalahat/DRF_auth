from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import Skyscraper

# Create your tests here.


class SkyscrapersTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        testuser1 = User.objects.create_user(username="Saleh", password="abc123")
        testuser1.save()

        # Create a blog Skyscraper
        test_skyscraper = Skyscraper.objects.create(
            owner=testuser1, 
            name="Burj Khalifa", 
            discription="one of the skyscrapers, and consederd the highest in the world", 
            height = 350,
            floors = 250
        )
        test_skyscraper.save()

    def test_skyscrapers_info(self):
        skys = Skyscraper.objects.get(id=1)
        expected_owner = f"{skys.owner}"
        expected_name = f"{skys.name}"
        expected_discription = f"{skys.discription}"
        expected_height = skys.height
        expected_floors = skys.floors
        self.assertEqual(expected_owner, "Saleh")
        self.assertEqual(expected_name, "Burj Khalifa")
        self.assertEqual(expected_discription, "one of the skyscrapers, and consederd the highest in the world")
        self.assertEqual(expected_height, 350)
        self.assertEqual(expected_floors, 250)

