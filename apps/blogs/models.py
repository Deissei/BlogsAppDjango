from django.db import models

from apps.author.models import Author


class Blog(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
    )
    description = models.TextField(
        max_length=2000,
        verbose_name="Содержание"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f"{self.title}"
    
    
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
