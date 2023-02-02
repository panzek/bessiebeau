from django.shortcuts import render, redirect, reverse, get_object_or_404

from .forms import TestimonialForm

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


def edit_testimonial(request, testimonial_id):
    """ A view to to edit customer's testimonial """

    testimonial = Testimonial.objects.get(pk=testimonial_id)
    if request.method == 'POST':

        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    
    form = TestimonialForm(instance=testimonial)

    context = {
        'form': form,
    }

    return render(request, 'testimonials/edit_testimonial.html', context)