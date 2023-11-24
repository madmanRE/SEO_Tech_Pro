from django.db import models


class AskLetter(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    mail = models.EmailField(verbose_name="Почта")
    message = models.TextField(blank=True, null=True, verbose_name="Текст")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано")

    def __str__(self):
        return f"{self.mail}: {self.message[0:25]}..."

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ["-is_read"]
