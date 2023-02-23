from django.contrib import admin

from testimonials.models import Testimonial

# Register models here.
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    """ Add Testimonial model to admin page"""
    list_filter = ('created_on', 'approved',)
    list_display = ('name', 'body', 'created_on', 'approved', 'user',)
    search_fields = ('name', 'email', 'body',)
    actions = ['approve_testimonials']

    def approve_testimonials(self, request, queryset):
        queryset.update(approved=True)
