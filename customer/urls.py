from django.urls import path
from . import views
app_name='customer'

urlpatterns = [
   path('basket/',views.basket,name='basket'),
   path('contact/',views.contact,name='contact'),
   path('login/',views.login_view,name='login'),
   path('register/',views.register,name='register'),
   path('logout/',views.logout_view,name='logout'),
   path('wishlist/',views.wishlist_view,name='wishlist'),
   path('wish_product/<int:pk>/',views.wish_product,name='wish_product'),
   path('unwish_product/<int:pk>/',views.unwish_product,name='unwish_product'),
   path('add-basket/<int:product_pk>/',views.add_basket,name='add-basket'),
   path('increase-basket-item/<int:basket_pk>/',views.increase_basket_item,name='increase-basket-item'),
   path('decrease-basket-item/<int:basket_pk>/',views.decrease_basket_item,name='decrease-basket-item'),
   path('remove-basket/<int:basket_pk>/',views.remove_basket,name='remove-basket'),
   path('change-currency/', views.change_currency, name='change-currency'),
]
