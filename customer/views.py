from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request, 'customer_template/home.html')

def customer_cart(request):
    return render(request, 'customer_template/cart.html')

def customer_product_details(request):
    return render(request, 'customer_template/product_details.html')
