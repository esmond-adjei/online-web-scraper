# Generated by Django 4.1 on 2022-12-17 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_movie_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermovie',
            old_name='user_moviename',
            new_name='user_movie',
        ),
    ]
