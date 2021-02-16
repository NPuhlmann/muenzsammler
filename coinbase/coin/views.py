from coin.models import Coin
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from .models import ImageCoin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse

# Create your views here.


class ImageCoinListView(LoginRequiredMixin, ListView):
    model = ImageCoin

    def get_queryset(self):
        return ImageCoin.objects.filter(user=self.request.user)


class ImageCoinCreateView(LoginRequiredMixin, CreateView):
    model = ImageCoin
    fields = [
        'name', 'image'
    ]

    def get_success_url(self):
        return reverse('coins:imagecoin_list')

    def form_valid(self, form):
        imagecoin = form.save(commit=False)
        imagecoin.user = self.request.user
        imagecoin.save()
        return super(ImageCoinCreateView, self).form_valid(form)


class ImageCoinDetailView(LoginRequiredMixin, DetailView):
    model = ImageCoin
    context_object_name = 'imagecoin'

    def get_queryset(self):
        return ImageCoin.objects.filter(user=self.request.user)


class CoinCreateView(LoginRequiredMixin, CreateView):
    model = Coin
    fields = ['name', 'material', 'reihe', 'weight', 'year']

    def get_success_url(self):
        return reverse('coins:imagecoin_list')

    def form_valid(self, form):
        coin = form.save(commit=False)
        coin.user = self.request.user
        coin.save()

        image = ImageCoin(name=coin.name,
                          user=self.request.user, coin=coin, image='coins/sentence.png')
        image.save()
        return super(CoinCreateView, self).form_valid(form)


class CoinDeleteView(LoginRequiredMixin, DeleteView):
    model = Coin

    def get_success_url(self):
        return reverse('coins:imagecoin_list')
