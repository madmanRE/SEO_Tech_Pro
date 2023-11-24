from django.db import models
from django.db.models import Count


class BlogCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name="Название")
    slug = models.SlugField(verbose_name="Символьный код")

    def __str__(self):
        return self.title

    def count_items(self):
        return self.items.count()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["-id"]


class BlogPost(models.Model):
    category = models.ForeignKey(
        BlogCategory,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name="Категория",
    )
    title = models.CharField(max_length=250, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Символьный код")
    image = models.URLField(verbose_name="Основное изображение")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    text = models.TextField(verbose_name="Основной контент")
    views = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")
    is_active = models.BooleanField(default=True, verbose_name="Доступность")

    def __str__(self):
        return self.title

    def add_view(self):
        self.views += 1

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-id"]

    def soft_delete(self):
        self.is_active = False
        self.save()
