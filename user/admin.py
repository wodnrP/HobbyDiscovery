from django.contrib import admin
from .models import User, Subscription, Sub_pd

# Register your models here.
admin.site.register(User)
admin.site.register(Subscription)
admin.site.register(Sub_pd)
