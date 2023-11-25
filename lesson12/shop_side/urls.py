from django.urls import path
from .views import *

urlpatterns = [
    path('product-create/', product_create_view, name='product_create'),
]