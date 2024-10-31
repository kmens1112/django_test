from django.urls import path 
from .views import *

app_name = 'djangoBooks'

urlpatterns = [
    path('', books_list.as_view(), name='list'),
    path('detail', books_detail.as_view(), name='detail'),
]