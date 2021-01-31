from django.urls import path

from .views import CoinListView

urlpatterns = [
    path('', CoinListView.as_view(
        template_name='coins/coin_list.html'), name='coinlist-view'),
]
