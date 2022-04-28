import imp
from django.shortcuts import render
from .forms import SignupForm
from django.contrib.auth import login,authenticate


# Create your views here.
def home(request):
    return render(request, 'home.html')

def aboutuspage(request):
    return render(request, 'about.html')

def servicepage(request):
    return render(request, 'services.html')

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