# Generated by Django 4.2.3 on 2023-08-10 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0016_coupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='used_customers',
            field=models.ManyToManyField(blank=True, related_name='used_coupons', to='customer.customer'),
        ),
    ]
