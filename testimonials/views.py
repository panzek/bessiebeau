from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import TestimonialForm

from testimonials.models import Testimonial
from profiles.models import UserProfile


def add_testimonial(request):
    """ A view to render the testimonial contents page """

    if request.method == 'POST':

        form = TestimonialForm(request.POST)
        if form.is_valid():
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            return redirect(reverse('home'))
    
    form = TestimonialForm()

    context = {
        'form': form,
    }

    return render(request, 'testimonials/add_testimonial.html', context)


def edit_testimonial(request, testimonial_id):
    """ A view to to edit customer's testimonial """

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.user != testimonial.user:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    
    form = TestimonialForm(instance=testimonial)

    context = {
        'form': form,
        'user_profile': user,
    }

    return render(request, 'testimonials/edit_testimonial.html', context)


def delete_testimonial(request, testimonial_id):
    """ A view to delete customer's testimonial """

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if request.user != testimonial.user:
        return redirect(reverse('home'))

    testimonial.delete()
    return redirect(reverse('home'))