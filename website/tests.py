from django.test import TestCase
from django.urls import reverse
from phrasebook.models import PhrasebookPhrase, PhrasebookSection

from .models import ProjectInfo


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


class AboutPageTests(TestCase):
    def test_about_page_shows_project_info(self):
        info = ProjectInfo.objects.create(content='Test project info')
        response = self.client.get(reverse('about'))
        self.assertContains(response, 'Test project info')


class PhrasebookPageTests(TestCase):
    def test_phrasebook_page_lists_sections_and_phrases(self):
        section = PhrasebookSection.objects.create(name='Приветствия')
        PhrasebookPhrase.objects.create(
            section=section,
            text='Салам алейкум',
            translation='Здравствуйте',
            translit='salam aleikum',
        )

        response = self.client.get(reverse('phrasebook'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('sections', response.context)
        self.assertContains(response, 'Приветствия')
        self.assertContains(response, 'Салам алейкум')
        self.assertContains(response, 'Здравствуйте')
        self.assertContains(response, 'salam aleikum')
