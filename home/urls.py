from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy_policy/', views.privacy_policy, name='privacy'),
    path('refund_policy/', views.refund_policy, name='refund'),
    path('terms_of_service/', views.terms_of_service, name='terms'),
    path('delivery_returns/', views.delivery_returns, name='delivery_returns'),
]
