from django.contrib import admin
from .models import Order, Order_detail
# Register your models here.
admin.site.register(Order)
admin.site.register(Order_detail)