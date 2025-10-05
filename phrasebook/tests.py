from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from .models import PhrasebookSection, PhrasebookPhrase


class PhrasebookAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.greetings = PhrasebookSection.objects.create(name="Greetings")
        self.travel = PhrasebookSection.objects.create(name="Travel")

        self.hello = PhrasebookPhrase.objects.create(
            section=self.greetings,
            text="Валейкум ас-салам",
            translation="Hello",
            translit="Valeykum as-salam",
        )
        self.how_are_you = PhrasebookPhrase.objects.create(
            section=self.greetings,
            text="Къвай хӏун?",
            translation="How are you?",
            translit="Q'way hün?",
        )
        self.ticket = PhrasebookPhrase.objects.create(
            section=self.travel,
            text="Цу билет гьиди?",
            translation="Where is my ticket?",
            translit="Tsu bilet ghidi?",
        )

    def test_sections_list_includes_nested_phrases(self):
        url = reverse("phrasebooksection-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        sections_by_id = {section["id"]: section for section in response.data}
        self.assertIn(self.greetings.id, sections_by_id)

        greetings = sections_by_id[self.greetings.id]
        self.assertEqual(greetings["name"], "Greetings")
        self.assertEqual(len(greetings["phrases"]), 2)

        hello_phrase = next(
            phrase for phrase in greetings["phrases"] if phrase["id"] == self.hello.id
        )
        self.assertEqual(hello_phrase["text"], self.hello.text)
        self.assertEqual(hello_phrase["translation"], self.hello.translation)
        self.assertEqual(hello_phrase["translit"], self.hello.translit)

    def test_filter_phrases_by_section(self):
        url = reverse("phrasebookphrase-list")
        response = self.client.get(url, {"section_id": self.greetings.id})

        self.assertEqual(response.status_code, 200)
        phrases = {phrase["id"] for phrase in response.data}
        self.assertEqual(phrases, {self.hello.id, self.how_are_you.id})
