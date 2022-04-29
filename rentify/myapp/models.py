#categories/models.py
import email
from operator import mod, truediv
from django.db import models

#class Categories(models.Model):
 #   name = models.CharField(max_length=200)
  #  description = models.TextField()

   # def __str__(self):
    #    return self.name

from django.contrib.auth.models import User

class Customer(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, on_delete=models.CASCADE)
    Fname = models.CharField(max_length=200, null=True)
    Lname = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length= 200)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    


    def __str__(self): # -> str:
        return self.email

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	available = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url

#class Packages():



#class Inventory():



#class Rent():


class Payment(models.Model):
    transaction_id = models.CharField(max_length=200, null=True)





class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    #image
    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null= True, blank= True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    pincode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
#class Refund():


#class feedback():


