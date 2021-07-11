from django.urls import path
from . import views
from AppShopStore.views import Homepage

app_name = 'AppShopStore'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
]
