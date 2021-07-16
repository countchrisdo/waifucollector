from django.contrib import admin
from .models import Cameo, Waifu, Accessory, Photo

# Register your models here.
admin.site.register(Waifu)
admin.site.register(Cameo)
admin.site.register(Accessory)
admin.site.register(Photo)