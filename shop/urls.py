from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('',views.index,name='index'),
    path('detail/',views.detail,name='detail'),
    path('shop/',views.shop,name='shop'),
]
