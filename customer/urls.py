from django.urls import path
from . import views


urlpatterns=[
    path('home',views.customer_home),
    path('cart',views.customer_cart),
    path('product_details',views.customer_product_details)
     ]
