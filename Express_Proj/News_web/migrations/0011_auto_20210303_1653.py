# Generated by Django 3.1 on 2021-03-03 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('News_web', '0010_socialmedias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedias',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_email', to=settings.AUTH_USER_MODEL),
        ),
    ]
