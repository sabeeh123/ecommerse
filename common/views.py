from django.shortcuts import render

# Create your views here.
def common_index(request):
    return render(request,'common_templates/index.html')

def common_name(request):
    return render(request,'common_templates/name.html')

def common_seller(request):
    return render(request,'common_templates/seller_login.html')   

def common_customer(request):
    return render(request,'common_templates/customer_login.html')

def common_seller_signup(request):
    return render(request,'common_templates/seller_signup.html')

def common_customersignup(request):
    return render(request,'common_templates/customersignup.html')

def common_changepassword(request):
    return render(request,'common_templates/changepassword.html')