# Generated by Django 4.2.3 on 2023-08-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_category_similiar_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='similar_products',
            field=models.ManyToManyField(blank=True, related_name='related_categories', to='shop.prouduct'),
        ),
    ]
