# Generated by Django 4.2.3 on 2023-08-03 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0004_alter_prouduct_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='prouduct',
            name='star_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='prouduct',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
