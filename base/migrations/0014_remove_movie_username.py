# Generated by Django 4.1 on 2022-12-17 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_usermovie_user_moviename'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='username',
        ),
    ]
