from django.db import models
from django.contrib.admin import display
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.urls import reverse
from shared.urlutilis import get_slug
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
    title = models.TextField(max_length=50)
    slug = models.CharField(max_length=100,blank=True)
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

    def save(self, *args, **kwargs):
        self.slug = get_slug(self.title)
        return super().save(*args, **kwargs)


    def get_similar_products(self):
        # similar_by_category = Prouduct.objects.filter(category__in=self.category.all()).exclude(pk=self.pk)

        similar_by_general = Prouduct.objects.filter(general__in=self.general.all()).exclude(pk=self.pk)

        return similar_by_general


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def get_avg_star(self):
        return self.reviews.aggregate(star_count_avg=models.Avg('star_count'))['star_count_avg'] or 0
    
    def get_absolute_url(self):
        return reverse("shop:product-detail", kwargs={"pk": self.pk, 'slug': self.slug})
    
    
    

class ProuductImages (models.Model):
    prouduct = models.ForeignKey(Prouduct,on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='images')

    
    @display(description="Movcud sekil")
    def image_tag(self):
        return format_html(f'<img width="200" src="{self.image.url}">')

    
   
    




