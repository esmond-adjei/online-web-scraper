# Generated by Django 4.1 on 2022-12-06 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_movie_delete_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movielink',
            field=models.TextField(blank=True, null=True),
        ),
    ]
