from django.contrib import admin
from django.urls import path

urlpatterns =[

   
    path('home',views.ecom_admin_home),
    path('login',views.ecom_admin_login),
    path('approve',views.ecom_admin_approve_seller),
    path('customer',views.ecom_admin_customer),
    path('seller',views.ecom_admin_seller)
   
]
