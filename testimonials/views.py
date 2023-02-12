from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse, get_object_or_404


from .forms import TestimonialForm

from testimonials.models import Testimonial
from profiles.models import UserProfile


@login_required(login_url='/accounts/login/')
def add_testimonial(request):
    """ A view to render the testimonial contents page """

    user = get_object_or_404(UserProfile, user=request.user)
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user.username
            testimonial = form.save(commit=False)
            testimonial.user = request.user
            testimonial.save()
            messages.success(
                request, "Your testimonial successfully submitted, but awaiting approval. Thank You!"
                )
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add testimonial. Please ensure the form is valid')
    else:
        form = TestimonialForm()

    context = {
        'form': form,
        'user_profile': user,
    }

    return render(request, 'testimonials/add_testimonial.html', context)

@login_required(login_url='/accounts/login/')
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
            messages.success(request, 'Successfully updated your testimonial!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to update testimonial. Please ensure the form is valid')
    else:
        form = TestimonialForm(instance=testimonial)

    context = {
        'form': form,
        'user_profile': user,
    }

    return render(request, 'testimonials/edit_testimonial.html', context)

@login_required(login_url='/accounts/login/')
def delete_testimonial(request, testimonial_id):
    """ A view for the user to delete testimonial created by that user"""

    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    
    if request.user != testimonial.user:
        return redirect(reverse('home'))
    
    if request.user.is_superuser:
        testimonial.delete()
        messages.success(request, 'Testimonial successfully deleted!')
       
    else:
        messages.error(request, 'Sorry, only staff members can delete testimonials')
    
    return redirect(reverse('home'))
