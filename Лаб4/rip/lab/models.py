from django.db import models

class NoteBook(models.Model):
    manufacturer = models.CharField("Производитель", max_length=50)
    name = models.CharField("Модель", max_length=50)
    display = models.IntegerField("Диагональ дисплея")
    os = models.CharField("Операционная система", max_length=50)
    image = models.ImageField("Изображение")
