from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request,'seller templates/sellerhome.html')

def cart(request):
    return render(request,'seller templates/cart.html')
