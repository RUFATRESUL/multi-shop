# Generated by Django 4.2.3 on 2023-08-02 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishitem',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishlist', to='customer.customer'),
        ),
    ]
