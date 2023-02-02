from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import TestimonialForm

from profiles.models import UserProfile
from testimonials.models import Testimonial


def add_testimonial(request):
    """ A view to render the testimonial contents page """

    if request.method == 'POST':

        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    
    form = TestimonialForm()

    context = {
        'form': form,
    }

    return render(request, 'testimonials/add_testimonial.html', context)