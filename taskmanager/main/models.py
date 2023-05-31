from django.db import models


class Task(models.Model):
    price = models.CharField("Цена вида протеза", max_length=7)
    name = models.TextField("Описание")
    image = models.ImageField(null=True)

    #Наша зуботехническая лаборатория занимается изготовлением разных зуботехнических изделий c 2012 года.Находимся по адресу г.Новосибирск, ул.Волховская 33\1. По условиям подробнее звоните по телефону и указанной почте 8-9180-423-50-44.

# Create your models here.
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Изделия"
        verbose_name_plural = "Изделия"

class About(models.Model):
    greeting = models.TextField("Приветствие")
    email = models.CharField("E-mail", max_length=50)
    tel = models.CharField("Телефон",  max_length=15)
    image = models.ImageField(null=True)
    def __str__(self):
        return self.greeting

    class Meta:
        verbose_name = "Приветствие"
        verbose_name_plural = "Приветствие"