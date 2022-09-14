from django.urls import path
from . import views


urlpatterns=[
    path('index',views.common_index),
    path('name',views.common_name)
]