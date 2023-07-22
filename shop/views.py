from django.shortcuts import render
from .models import Category,Company,Prouduct,ProuductImages
from django.db.models import Count
# Create your views here.

def index(request):
    slide_company = Company.objects.filter(is_slide=True)[:3]
    nonslide_company = Company.objects.filter(is_slide=False)[:4]
    categories = Category.objects.annotate(prouduct_count=Count('prouduct'))
    new_product = Prouduct.objects.all().order_by('-created')[:8]
    featured_products = Prouduct.objects.filter(featured=True)
    return render(request,'index.html',{
       'slide_company':slide_company,
       'nonslide_company':nonslide_company,
       'categories':categories,
       'new_product':new_product,
       'featured_products':featured_products,
       
       
    })

def detail(request):
    return render(request,'detail.html')

def shop(request):
    return render(request,'shop.html')
