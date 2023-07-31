from django.urls import path
from . import views
app_name='customer'

urlpatterns = [
   path('cart/',views.cart,name='cart'),
   path('contact/',views.contact,name='contact'),
   path('login/',views.login_view,name='login'),
   path('register/',views.register,name='register'),
   path('logout/',views.logout_view,name='logout'),
   path('wishlist/',views.wishlist,name='wishlist'),
   path('wish_product/<int:pk>/',views.wish_product,name='wish_product'),
   path('unwish_product/<int:pk>/',views.unwish_product,name='unwish_product')
]
