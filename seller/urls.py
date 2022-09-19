from django.urls import path
from . import views


urlpatterns=[
    path('sellerhome', views.seller_home),
    path('cart',views.cart),
    path('addproduct',views.addproduct),
    path('changepassword',views.changepassword),
    path('myorders',views.myorders),
    path('update_stock',views.update_stock)
]
