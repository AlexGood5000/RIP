from django.db import models

class Manufacturers(models.Model):
    name_man = models.CharField('Имя производителя', max_length=200)

class Details(models.Model):
    name_det = models.CharField('Наименование детали', max_length=200)
    cost_det = models.IntegerField('Цена детали', default=0)
    mans = models.ForeignKey(Manufacturers, models.DO_NOTHING)