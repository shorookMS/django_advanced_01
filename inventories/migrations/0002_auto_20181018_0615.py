# Generated by Django 2.0.7 on 2018-10-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='is_empty',
            field=models.BooleanField(choices=[(1, 'Empty'), (2, 'Not Empty')]),
        ),
    ]
