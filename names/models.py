from django.db import models


class NameCategory(models.Model):
    """A grouping for Avar names, e.g. female names or historical figures."""

    name = models.CharField('Название категории', max_length=128, unique=True)
    description = models.TextField('Описание', blank=True)
    order = models.PositiveIntegerField('Порядок отображения', default=0)

    class Meta:
        verbose_name = 'Категория имён'
        verbose_name_plural = 'Категории имён'
        ordering = ['order', 'name']

    def __str__(self) -> str:
        return self.name


class AvarName(models.Model):
    """An individual Avar name with translations and metadata."""

    class Gender(models.TextChoices):
        MALE = 'male', 'Мужское'
        FEMALE = 'female', 'Женское'
        UNISEX = 'unisex', 'Универсальное'

    category = models.ForeignKey(
        NameCategory,
        on_delete=models.CASCADE,
        related_name='names',
        verbose_name='Категория',
    )
    name = models.CharField('Имя на аварском', max_length=128)
    translation = models.CharField(
        'Перевод',
        max_length=256,
        help_text='Значение имени или эквивалент на русском/английском',
    )
    translit = models.CharField('Транслитерация', max_length=128, blank=True)
    gender = models.CharField(
        'Пол',
        max_length=10,
        choices=Gender.choices,
        default=Gender.UNISEX,
    )
    notes = models.TextField('Примечания', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)

    class Meta:
        verbose_name = 'Аварское имя'
        verbose_name_plural = 'Аварские имена'
        ordering = ['category', 'name']
        unique_together = ('category', 'name', 'gender')

    def __str__(self) -> str:
        return f"{self.name} ({self.get_gender_display()})"
