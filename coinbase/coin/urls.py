from django.urls import path

from .views import CoinDeleteView, ImageCoinListView, CoinCreateView, ImageCoinDetailView

app_name = 'coins'

urlpatterns = [
    path('', ImageCoinListView.as_view(
        template_name='coins/image-coin_list.html'), name='imagecoin_list'),
    path('create/', CoinCreateView.as_view(
        template_name='coins/image-coin_create.html'), name='imagecoin_create'),
    path('<int:pk>/', ImageCoinDetailView.as_view(
        template_name="coins/image-coin_detail.html"), name='imagecoin_detail'),
    path('<int:pk>/delete/', CoinDeleteView.as_view(
        template_name='coins/coin-check_delete.html'), name='coin_delete')
]
