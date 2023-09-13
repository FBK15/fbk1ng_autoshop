from django.urls import path
from main.views import stocks, developer

app_name = 'main'

urlpatterns = [
    path('', stocks, name='stocks'),
    path('developer_identity/', developer, name='developer_identity'),
]