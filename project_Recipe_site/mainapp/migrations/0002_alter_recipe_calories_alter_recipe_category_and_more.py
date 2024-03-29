# Generated by Django 4.2.6 on 2024-02-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.CharField(max_length=5, verbose_name='Калорийность'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='category',
            field=models.ManyToManyField(to='mainapp.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.CharField(max_length=20, verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='portions',
            field=models.CharField(max_length=2, verbose_name='Количество порций'),
        ),
    ]
