from django.forms import ModelForm, TextInput, Textarea

from mainapp.models import Category, Recipe


class CreateRacipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'cooking_steps', 'cooking_time', 'img', 'category', 'calories', 'portions']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название рецепта',
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание рецепта'
            }),
            'ingredients': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ингредиенты'
            }),
            'cooking_steps': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Шаги приготовления'
            })
        }
        