from django.urls import path
from . import views

app_name="common"
urlpatterns=[
    path('',views.common_index),
    path('name',views.common_name,name='name'),
    path('seller_login',views.common_seller,name='login'),
    path('customer_login',views.common_customer),
    path('seller_signup',views.common_seller_signup),
    path('customersignup',views.common_customersignup,name='signup'),
    path('changepassword',views.common_changepassword)
    ]