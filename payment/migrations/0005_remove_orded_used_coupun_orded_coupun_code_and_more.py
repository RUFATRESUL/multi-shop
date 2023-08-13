# Generated by Django 4.2.3 on 2023-08-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_orded_phone_code_alter_orded_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orded',
            name='used_coupun',
        ),
        migrations.AddField(
            model_name='orded',
            name='coupun_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orded',
            name='coupun_discount',
            field=models.IntegerField(default=20),
        ),
    ]
