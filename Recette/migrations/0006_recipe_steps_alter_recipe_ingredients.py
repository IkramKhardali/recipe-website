# Generated by Django 4.1.7 on 2023-05-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recette', '0005_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='Steps',
            field=models.TextField(default='no Steps found'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(default='no ingredients found'),
        ),
    ]
