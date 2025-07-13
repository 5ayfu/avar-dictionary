from django.test import TestCase
from django.urls import reverse


class StaticPagesTests(TestCase):
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

    def test_visitor_context(self):
        response = self.client.get(reverse('home'))
        self.assertIn('active_visitors', response.context)
        self.assertIn('unique_visitors_today', response.context)
