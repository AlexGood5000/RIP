from django.db import models

class Manufacturer(models.Model):
    name = models.CharField("Производитель", max_length=50)
    country = models.CharField("Страна", max_length=50)

class NoteBook(models.Model):
    manuf = models.ForeignKey(Manufacturer, models.DO_NOTHING)
    name = models.CharField("Модель", max_length=50)
    display = models.IntegerField("Диагональ дисплея")
    ram = models.IntegerField("Оперативная паямять")
    os = models.CharField("Операционная система", max_length=50)
    image = models.ImageField("Изображение")