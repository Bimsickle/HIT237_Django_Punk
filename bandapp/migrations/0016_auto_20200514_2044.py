# Generated by Django 3.0.3 on 2020-05-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0015_auto_20200514_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='image_url',
            field=models.URLField(blank=True, default='https://bit.ly/2WT4gop'),
        ),
    ]