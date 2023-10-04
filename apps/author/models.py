from django.db import models


class Author(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name="Имя",
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name="Фамилия",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Почта",
    )
    
    def __str__(self):
        return f"{self.first_name}"
    
    
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"
