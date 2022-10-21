from django.contrib import admin
from .models import Hobby, Review, HobbyImage, Review_Image
# admin : HobbyDiscovery 220921
# Register your models here.

admin.site.register(Hobby)
admin.site.register(HobbyImage)
admin.site.register(Review)
admin.site.register(Review_Image)

