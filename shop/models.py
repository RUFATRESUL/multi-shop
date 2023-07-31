from django.db import models
from django.contrib.admin import display
from django.utils.html import format_html
# Create your models here.

class Size(models.Model):
    title = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.title
    

class Color(models.Model):
    title = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.title

class GeneralCategory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='categories')
    general_category = models.ForeignKey(GeneralCategory,on_delete=models.SET_NULL,null=True,blank=True,related_name='sub_categories')

    def __str__(self):
        return self.title

class Company(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='company')
    is_slide = models.BooleanField(default=False)
    discount_percent = models.FloatField()

    def __str__(self):
        return self.title

class Prouduct(models.Model):
    title = models.CharField(max_length=50)
    old_price = models.FloatField(null=True,blank=True)
    featured = models.BooleanField(default=False)
    price = models.FloatField()
    description = models.TextField()
    sizes = models.ManyToManyField(Size,related_name='prouduct')
    colors = models.ManyToManyField(Color,related_name='product')
    category = models.ManyToManyField(Category,related_name='prouduct')
    company = models.ManyToManyField(Company,related_name='product')
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    general = models.ManyToManyField(GeneralCategory,related_name='prouduct')
    def __str__(self):
        return self.title

class ProuductImages (models.Model):
    prouduct = models.ForeignKey(Prouduct,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images')

    
    @display(description="Movcud sekil")
    def image_tag(self):
        return format_html(f'<img width="200" src="{self.image.url}">')

    
   
    




