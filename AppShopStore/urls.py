from django.urls import path
from . import views
from AppShopStore.views import Homepage, add_to_cart

app_name = 'AppShopStore'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('cart/', add_to_cart.as_view(), name='Cart'),
]
