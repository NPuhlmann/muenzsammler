from coin.models import Coin
from django.shortcuts import render
from django.views.generic import ListView
from .models import ImageCoin

# Create your views here.


class CoinListView(ListView):
    model = ImageCoin
