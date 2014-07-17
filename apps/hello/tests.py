from django.test import TestCase
from django.shortcuts import get_object_or_404

from apps.hello.models import Info

# Create your tests here.

class MyInfoTestCase(TestCase):

    def setUp(self):
        self.info = {
                "name": "Andrey",
                "surname": "Panchenko",
                "bio": "I am from Ukraine...",
                "mail": "andy.punch@yandex.ru"
            }


    def test_create(self):
        test_person = get_object_or_404(Info, pk=1)
        self.assertDictContainsSubset(self.info, test_person.__dict__)

    def test_db(self):
        self.assertEqual(Info.objects.all().count(), 1)

    def test_view_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
