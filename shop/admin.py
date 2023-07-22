from django.contrib import admin

from .models import Size,Color,GeneralCategory,Category,Company,Prouduct,ProuductImages


# class ProductImageInline(admin.TabularInline):
#     model=ProuductImages
#     readonly_fields=['image_tag']
#     extra=1

# @admin.register(Prouduct)
# class ProductAdmin(admin.ModelAdmin):
#     inlines=[ProductImageInline]

# Register your models here.
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(GeneralCategory)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Prouduct)
admin.site.register(ProuductImages)
