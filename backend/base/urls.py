from django.urls import path
from .views import *

urlpatterns = [
    path('', getRouters, name='routes'),
    path('products/', getProducts, name='products'),
    path('product/<str:pk>/', getProduct, name='product'),

    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),


    path('users/profile/', getUserProfile, name='users-profile'),
    path('users/profile/update/', updateUserProfile, name='users-profile-update'),
    path('users/', getUsers, name='users'),

    path('users/register/', registerUser, name='register'),

    path('orders/add/', addOrderItems, name='orders-add'),
]