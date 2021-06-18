from django.urls import path
from . import views

app_name = 'UserApp'
urlpatterns = [
    path('singup/', views.SingUp, name='sing_up'),
    path('login/', views.Login, name='log_in'),
    path('logout/', views.LogOUt, name='log_out'),
]
