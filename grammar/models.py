from django.db import models
from dictionary.models import Language

class GrammarArticle(models.Model):
    title = models.CharField('Заголовок', max_length=256)
    content = models.TextField('Содержимое')
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='grammar_articles', verbose_name='Язык')
    section = models.CharField('Раздел', max_length=128, blank=True, help_text="Раздел: грамматика, фонетика, морфология и т.д.")
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Изменено', auto_now=True)

    class Meta:
        verbose_name = 'Грамматическая статья'
        verbose_name_plural = 'Грамматические статьи'
        ordering = ['language', 'section', 'title']

    def __str__(self):
        return f"{self.title} [{self.language.code}]"
