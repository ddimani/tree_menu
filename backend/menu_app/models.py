from django.db import models


class Menu(models.Model):
    """Модель меню."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        """Настройки метаданных для модели Menu."""

        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        """Возвращает строковое представление объекта Menu."""
        return self.name


class MenuItem(models.Model):
    """Модель элемента меню."""

    title = models.CharField(max_length=100, verbose_name="Заголовок")
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='submenu',
        on_delete=models.CASCADE
    )
    slug = models.CharField(max_length=255, verbose_name='Идентификатор')

    class Meta:
        """Настройки метаданных для модели MenuItem."""

        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункты меню"

    def __str__(self):
        """Возвращает строковое представление объекта MenuItem."""
        return self.title
