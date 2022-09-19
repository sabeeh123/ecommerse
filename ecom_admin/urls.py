from django.contrib import admin
from django.urls import path
from . import views

urlpatterns =[

    path('login',views.ecom_admin_login),
    path('approve',views.ecom_admin_approve_seller),
    path('customer',views.ecom_admin_customer),
    path('seller',views.ecom_admin_seller),
    path('home',views.ecom_admin_home)
   
]
