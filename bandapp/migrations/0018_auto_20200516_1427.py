# Generated by Django 3.0.3 on 2020-05-16 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0017_band_bio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='band',
            options={'ordering': ['band_name']},
        ),
        migrations.AlterField(
            model_name='band',
            name='bio',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
