from django.urls import path
from . import views

app_name = 'AppShopStore'
urlpatterns = [
    path('', views.Homepage, name='homepage'),
]
