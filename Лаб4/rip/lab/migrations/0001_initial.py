# Generated by Django 4.0.1 on 2022-01-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50, verbose_name='Производитель')),
                ('name', models.CharField(max_length=50, verbose_name='Модель')),
                ('display', models.IntegerField(verbose_name='Диагональ дисплея')),
                ('os', models.CharField(max_length=50, verbose_name='Операционная система')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
            ],
        ),
    ]
