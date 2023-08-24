from django.contrib import sitemaps
from django.urls import reverse
from shop.models import Prouduct




class StaticViewSitemap(sitemaps.Sitemap):


    def items(self):
        return [
            'shop:index',
            'shop:shop',
            'customer:contact',
            'customer:login',
            'customer:register'
        ]

    def location(self, item):
        return reverse(item)
    
    prorities = {
        'shop:index':0.9,
        'shop:shop':0.4,
        'customer:contact':0.6,
        'customer:login':0.5,
        'customer:register' :0.5,
    }

    def priority(self,item):
        return self.prorities[item]
    
    changefreqs = {
        'shop:index':'always',
        'shop:shop':'always',
        'customer:contact':'monthly',
        'customer:login':'yearly',
        'customer:register':'yearly',
    }


    def changefreq(self,item):
        return self.changefreqs[item]
    
class ProductViewSitemap(sitemaps.Sitemap):
    priority = 0.9
    changefreq = 'daily'
    
    def items(self):
        return Prouduct.objects.all()
    
    def lastmod(self,item):
        return item.update

