from django.db import models
from django.contrib.auth.models import User
from shop.models import Prouduct
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class WishItem(models.Model):
    product = models.ForeignKey(Prouduct,on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='wishlist')
    created = models.DateField(auto_now_add=True)
    
 
class BasketItem(models.Model):
    product = models.ForeignKey(Prouduct,on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='basketlist')
    count = models.IntegerField(default=0)
    size = models.ForeignKey('shop.Size',on_delete=models.CASCADE)
    color = models.ForeignKey('shop.Color',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.get_full_name()


    
class Review(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='reviews')
    product = models.ForeignKey(Prouduct,on_delete=models.CASCADE,related_name='reviews')
    comment = models.TextField()
    star_count = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created = models.DateField(auto_now_add=True)

class Reply(models.Model):
    review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='reply_comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateField(auto_now_add=True)


    