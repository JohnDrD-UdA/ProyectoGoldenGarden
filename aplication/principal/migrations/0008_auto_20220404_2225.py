# Generated by Django 2.2.14 on 2022-04-05 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0007_auto_20220404_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='usuario',
            field=models.ForeignKey(default='<django.db.models.query_utils.DeferredAttribute object at 0x000001D54A0383D0>', on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL),
        ),
    ]
