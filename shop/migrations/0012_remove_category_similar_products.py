# Generated by Django 4.2.3 on 2023-08-19 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_category_similar_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='similar_products',
        ),
    ]
