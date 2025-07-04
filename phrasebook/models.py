from django.db import models

class PhrasebookSection(models.Model):
    name = models.CharField('Название темы', max_length=128, unique=True)

    class Meta:
        verbose_name = 'Тема разговорника'
        verbose_name_plural = 'Темы разговорника'
        ordering = ['name']

    def __str__(self):
        return self.name

class PhrasebookPhrase(models.Model):
    section = models.ForeignKey(PhrasebookSection, on_delete=models.CASCADE, related_name='phrases')
    text = models.TextField('Текст', help_text="Фраза на аварском")
    translation = models.TextField('Перевод', help_text="Перевод (русский/английский)")
    translit = models.CharField('Транслитерация', max_length=128, blank=True, help_text="Транслитерация (если есть)")

    class Meta:
        verbose_name = 'Phrasebook Phrase'
        verbose_name_plural = 'Phrasebook Phrases'
        ordering = ['section', 'id']
        unique_together = ('section', 'text')

    def __str__(self):
        return f"{self.text} ({self.section})"
