from django.contrib import admin
from .models import Contact,Customer,ResetPassword
# Register your models here.
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(ResetPassword)
