# Generated by Django 3.0.3 on 2020-05-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bandapp', '0004_auto_20200507_2131'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Member',
        ),
    ]