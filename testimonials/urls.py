from django.urls import path
from . import views

urlpatterns = [
    path('add_testimonial/', views.add_testimonial, name='testimonial'),
]