# Generated by Django 4.2.3 on 2023-08-08 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_basketitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketitem',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
