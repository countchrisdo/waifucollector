# Generated by Django 3.2.3 on 2021-07-16 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='waifu',
        ),
    ]