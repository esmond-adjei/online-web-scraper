# Generated by Django 4.1 on 2022-12-18 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_rename_user_moviename_usermovie_user_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imagelink',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
