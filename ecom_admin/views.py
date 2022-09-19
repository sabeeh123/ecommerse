from django.shortcuts import render

# Create your views here.

def ecom_admin_login(request):
    return render(request,'admin_templates/login.html')

def ecom_admin_approve_seller(request):
    return render(request,'admin_templates/approve_seller.html')    

def ecom_admin_customer(request):
    return render(request,'admin_templates/view_customer.html')  

def ecom_admin_seller(request):
    return render(request,'admin_templates/view_seller.html')      

def ecom_admin_home(request):
    return render(request,'admin_templates/home.html')    