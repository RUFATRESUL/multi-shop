from django import template
from ..models import GeneralCategory,Category
from customer.models import WishItem

register=template.Library()

@register.inclusion_tag('includes/nav-category.html')

def nav_category():
    pure_categories=Category.objects.filter(general_category__isnull=True)
    general_categories=GeneralCategory.objects.all()
    return {
        'pure_categories':pure_categories,
        'general_categories':general_categories,
    }

@register.inclusion_tag('includes/stars.html')

def stars(star_count):
    full_stars = int(star_count)
    half_stars = full_stars != star_count
    empty_stars = 5 - (full_stars + int(half_stars))
    return{
        'full_stars':range(full_stars),
        'half_stars':half_stars,
        'empty_stars':range(empty_stars),
    }

@register.filter
def is_wished(product,request):
    if not request.user.is_authenticated:
        return False
    
    return WishItem.objects.filter(product=product,customer=request.user.customer).exists()


@register.simple_tag
def get_querystring(request,key,value):
    querydict = request.GET.copy()
    querydict[key] = value
    querystring = querydict.urlencode()
    return '?'+ querystring
    