# Generated by Django 3.2.3 on 2021-07-15 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cameo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cameo',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='cameo',
            name='description',
            field=models.TextField(verbose_name='Describe their Cameo here'),
        ),
        migrations.AddField(
            model_name='waifu',
            name='accessories',
            field=models.ManyToManyField(to='main_app.Accessory'),
        ),
    ]
