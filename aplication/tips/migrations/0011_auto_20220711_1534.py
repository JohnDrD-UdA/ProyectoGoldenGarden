# Generated by Django 2.2.14 on 2022-07-11 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0010_auto_20220711_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='fecha_creacion',
            field=models.TextField(verbose_name=datetime.datetime.now),
        ),
    ]
