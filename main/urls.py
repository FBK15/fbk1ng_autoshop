from django.urls import path
from main.views import stocks

app_name = 'main'

urlpatterns = [
    path('', stocks, name='stocks'),
]