# Generated by Django 4.2.3 on 2023-08-11 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0017_alter_coupon_used_customers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Coupon',
        ),
    ]
