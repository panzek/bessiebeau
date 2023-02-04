from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('edit/<str:id>', views.edit_profile, name='edit_profile'),
    path('delete/<str:id>/', views.delete_profile, name='delete_profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('add_to_wishlist/<int:id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('delete_from_wishlist/<int:id>/', views.delete_from_wishlist, name='delete_from_wishlist'),
]
