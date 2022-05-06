import imp
from multiprocessing import context
from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import login,authenticate
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutuspage(request):
    return render(request, 'about.html')

def servicepage(request):
    return render(request, 'services.html')

def product(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products.html', context)
    
def products_HW(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products_HW.html', context)

def products_SW(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'products_SW.html', context)

def cart(request):

    if request.user.is_authenticated:
        user = request.user
        order, created = Order.objects.get_or_create(user=user, complete =True)
        items = Order.objects.all()
    else:
        items = []

    items = OrderItem.objects.all()
    context = {'items':items}
    return render(request, 'cart.html', context)

def renting(request):
    return render(request, 'renting.html')

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            pwd=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=pwd)
            login(request,user)
            
    form=SignupForm
    return render(request, 'registration/signup.html',{'form':form})