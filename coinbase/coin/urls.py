from django.urls import path

from .views import ImageCoinListView, CoinCreateView, ImageCoinDetailView

app_name = 'coins'

urlpatterns = [
    path('', ImageCoinListView.as_view(
        template_name='coins/image-coin_list.html'), name='imagecoin_list'),
    path('create/', CoinCreateView.as_view(
        template_name='coins/image-coin_create.html'), name='imagecoin_create'),
    path('<int:pk>/', ImageCoinDetailView.as_view(
        template_name="coins/image-coin_detail.html"), name='imagecoin_detail')
]
