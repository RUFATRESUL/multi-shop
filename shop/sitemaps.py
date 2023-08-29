from django.contrib import sitemaps
from django.urls import reverse


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
    
    prorities = {
        'shop:index':,
        'shop:shop':,
        'customer:contact':,
        'customer:login':,
        'customer:register' :,
    }


    def changefreq(self,item):
        pass
