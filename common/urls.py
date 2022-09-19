from django.urls import path
from . import views


urlpatterns=[
    path('',views.common_index),
    path('name',views.common_name),
    path('seller_login',views.common_seller),
    path('customer_login',views.common_customer),
    path('seller_signup',views.common_seller_signup),
    path('customersignup',views.common_customersignup),
    path('changepassword',views.common_changepassword)
    ]