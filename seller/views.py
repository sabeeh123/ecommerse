from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request,'seller_templates/sellerhome.html')

def cart(request):
    return render(request,'seller_templates/cart.html')

def addproduct(request):
    return render(request,'seller_templates/addproduct.html')

def myorders(request):
    return render(request,'seller_templates/myorders.html') 

def changepassword(request):
    return render(request,'seller_templates/changepassword.html')   

def update_stock(request):
    return render(request,'seller_templates/update_stock.html')    

