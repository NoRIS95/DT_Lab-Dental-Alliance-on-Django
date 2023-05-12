from django.db import models


class Task(models.Model):
    price = models.CharField("Цена вида протеза", max_length=7)
    name = models.TextField("Описание")

# Create your models here.
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изделия"
        verbose_name_plural = "Изделия"