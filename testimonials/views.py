from django.shortcuts import render


def add_testimonial(request):
    """ A view to render the cart contents page """

    return render(request, 'testimonials/add_testimonial.html')

