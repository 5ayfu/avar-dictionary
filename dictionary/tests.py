from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Language, Word, Synonym


class SynonymFilterTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.lang = Language.objects.create(code="av", name="Avar")
        self.word1 = Word.objects.create(text="a", language=self.lang)
        self.word2 = Word.objects.create(text="b", language=self.lang)
        self.word3 = Word.objects.create(text="c", language=self.lang)
        Synonym.objects.create(word1=self.word1, word2=self.word2)
        Synonym.objects.create(word1=self.word2, word2=self.word3)

    def test_filter_by_word_id(self):
        url = reverse("synonym-list") + f"?word_id={self.word2.id}"
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)

