from django.test import SimpleTestCase
from django.urls import reverse


class StaticPagesTests(SimpleTestCase):
    def test_pages_accessible(self):
        pages = [
            reverse('home'),
            reverse('dictionary'),
            reverse('phrasebook'),
            reverse('grammar'),
            reverse('names'),
            reverse('about'),
            reverse('contact'),
        ]

        for url in pages:
            with self.subTest(url=url):
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
