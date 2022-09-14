from django.urls import path
from . import views


urlpatterns=[
    path('sellerhome', views.seller_home),
    path('cart',views.cart)
]
