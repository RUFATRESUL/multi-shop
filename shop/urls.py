from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('products/<int:pk>/<str:slug>/', views.product_detail, name='product-detail'),
    path('review/<int:pk>/',views.review,name='review'),
    path('reply_review/<int:pk>/', views.reply_review, name='reply_review'),
     
]

