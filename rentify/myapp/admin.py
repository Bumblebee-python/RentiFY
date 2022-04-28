from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
#admin.site.register(Login)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Payment)
#admin.site.register(Customer)