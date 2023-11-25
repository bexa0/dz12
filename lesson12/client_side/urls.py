from django.urls import path
from client_side.views import *

urlpatterns = [
    path('', product_view, name='product_list'),
    path('product/<slug:product_slug>/', product_detail, name='product_detail'),
]