# Generated by Django 2.2.14 on 2022-04-05 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_auto_20220404_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
