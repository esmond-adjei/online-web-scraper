# Generated by Django 4.1 on 2022-11-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_moviedata_movielink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='imagelink',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
