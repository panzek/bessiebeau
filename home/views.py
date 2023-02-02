from django.shortcuts import render
from testimonials.models import Testimonial


def index(request):
    """ A view to render the home page """
    
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)
