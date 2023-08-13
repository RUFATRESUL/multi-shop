from django.contrib import admin
from .models import Coupon,Orded,OrderProduct
# Register your models here.
admin.site.register(Coupon)


class OrderProductsInline(admin.TabularInline):
    model = OrderProduct
    extra = 0

@admin.register(Orded)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductsInline]
