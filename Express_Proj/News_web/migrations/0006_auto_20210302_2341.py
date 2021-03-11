# Generated by Django 3.1 on 2021-03-02 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News_web', '0005_auto_20210130_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='soc_fb',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='soc_ig',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='author',
            name='soc_tw',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_published',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to='artcle_thumb'),
        ),
    ]
