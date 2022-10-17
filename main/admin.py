from django.contrib import admin
from .models import Hobby, review, HobbyImage
# admin : HobbyDiscovery 220921
# Register your models here.

admin.site.register(Hobby)
admin.site.register(HobbyImage)
admin.site.register(review)

