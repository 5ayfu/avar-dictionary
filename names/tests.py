from django.test import TestCase

from .models import AvarName, NameCategory


class NamesModelTests(TestCase):
    def test_name_str(self):
        category = NameCategory.objects.create(name='Женские имена')
        name = AvarName.objects.create(
            category=category,
            name='Патимат',
            translation='Fatimat',
            gender=AvarName.Gender.FEMALE,
        )

        self.assertIn('Патимат', str(name))
        self.assertIn('Женское', str(name))
