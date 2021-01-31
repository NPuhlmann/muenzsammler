from django.contrib import admin
from .models import Coin, SammlerReihe, ImageCoin

# Register your models here.
admin.site.register(Coin)
admin.site.register(SammlerReihe)
admin.site.register(ImageCoin)
