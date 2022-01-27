from django.urls import path
from .views import *

urlpatterns = [
    path('', getRouters, name='routes'),
    path('products/', getProducts, name='products'),
    path('product/<str:pk>/', getProduct, name='product'),
]