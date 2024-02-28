from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.core.validators import MinValueValidator
from django.db.models import Manager

User = get_user_model()


class Category(models.Model):
    """
    Модель Категорий на сайте
    """
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)
    objects = Manager()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Recipe(models.Model):
    """
    Модель рецептов на сайте
    """

    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ingredients = models.TextField(verbose_name='Ингредиенты')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.CharField(max_length=20, verbose_name='Время приготовления')
    img = models.ImageField(upload_to='recipe', blank=True, null=True, verbose_name='Изображение', validators=[
        FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))])
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='автор')
    category = models.ManyToManyField(Category, verbose_name='Категория')
    calories = models.CharField(max_length=10, verbose_name='Калорийность')
    portions = models.CharField(max_length=2, verbose_name='Количество порций')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    objects = Manager()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    @staticmethod
    def get_items():
        return Recipe.objects.filter(is_active=True).order_by('category', 'title')


class CategoryRecipe(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)