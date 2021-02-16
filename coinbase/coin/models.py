from django.db import models
from django.db.models.fields import CharField, IntegerField, FloatField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from django.conf import settings

# Create your models here.


class SammlerReihe(models.Model):
    name = CharField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name


class Coin(models.Model):
    MATERIAL_CHOICES = [
        ('go', 'Gold'),
        ('si', 'Silver'),
        ('ku', 'Kupfer'),
        ('br', 'Bronze'),
    ]

    name = CharField(max_length=200, unique=False, blank=True)
    material = CharField(max_length=2, choices=MATERIAL_CHOICES, default='go')
    year = IntegerField()
    reihe = ForeignKey(SammlerReihe, on_delete=models.CASCADE)
    weight = FloatField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # new
        on_delete=models.CASCADE,
        blank=False, null=True
    )

    def __str__(self):
        return self.name


class ImageCoin(models.Model):
    name = CharField(max_length=100)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    image = ImageField(upload_to='coins', blank=True, null=True)
    default = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # new
        on_delete=models.CASCADE,
        blank=False, null=True
    )

    def __str__(self):
        return self.coin.name + "_" + self.name
