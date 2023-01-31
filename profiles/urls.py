from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('edit/<str:id>', views.edit_profile, name='edit_profile'),
    path('delete/<str:id>/', views.delete_profile, name='delete_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist/', views.wishlist, name='wishlist'),
] 