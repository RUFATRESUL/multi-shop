# Generated by Django 4.2.3 on 2023-08-19 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_category_similiar_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='similiar_products',
        ),
    ]
