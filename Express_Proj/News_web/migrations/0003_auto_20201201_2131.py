# Generated by Django 3.1 on 2020-12-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_web', '0002_auto_20201201_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
