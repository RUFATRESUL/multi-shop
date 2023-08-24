from django.contrib import admin

from .models import Size,Color,GeneralCategory,Category,Company,Prouduct,ProuductImages
from customer.models import Review

class ProductImageInline(admin.TabularInline):
    model=ProuductImages
    readonly_fields=['image_tag']
    extra=1

class ReviewInline(admin.TabularInline):
    model = Review
    readonly_fields = ['customer','star_count','comment']
    extra=0

@admin.register(Prouduct)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline,ReviewInline]
    list_filter = ['general']
    readonly_fields = ['slug']

# Register your models here.
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(ProuductImages)

