from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),

    path('services',views.servicepage, name="servicepage"),

    path('about',views.aboutuspage, name="aboutuspage"),

    path('accounts/signup', views.signup, name="signup")
    
]
