# Generated by Django 4.2.3 on 2023-07-16 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='categories')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='company')),
                ('is_slide', models.BooleanField(default=False)),
                ('discount_percent', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GeneralCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Prouduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('old_price', models.FloatField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='prouduct', to='shop.category')),
                ('colors', models.ManyToManyField(related_name='product', to='shop.color')),
                ('company', models.ManyToManyField(related_name='product', to='shop.company')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProuductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('prouduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.prouduct')),
            ],
        ),
        migrations.AddField(
            model_name='prouduct',
            name='sizes',
            field=models.ManyToManyField(related_name='prouduct', to='shop.size'),
        ),
        migrations.AddField(
            model_name='category',
            name='general_categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.generalcategory'),
        ),
    ]
