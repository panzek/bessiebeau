from django.urls import path
from . import views

urlpatterns = [
    path('add_testimonial/', views.add_testimonial, name='testimonial'),
    path('edit_testimonial/<int:testimonial_id>', views.edit_testimonial, name='edit_testimonial'),
    path('delete_testimonial/<int:testimonial_id>', views.delete_testimonial, name='delete_testimonial'),
]
