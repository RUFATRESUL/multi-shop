# Generated by Django 4.2.3 on 2023-08-12 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_orded_orderproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orded',
            name='mobile',
            field=models.CharField(choices=[('+994', '+994'), ('+999', '+999'), ('+012', '+012')], max_length=20),
        ),
    ]
