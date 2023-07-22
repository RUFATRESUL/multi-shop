from django import template
from ..models import GeneralCategory,Category


register=template.Library()

@register.inclusion_tag('includes/nav-category.html')

def nav_category():
    pure_categories=Category.objects.filter(general_category__isnull=True)
    general_categories=GeneralCategory.objects.all()
    return {
        'pure_categories':pure_categories,
        'general_categories':general_categories,
    }
