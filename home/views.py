from django.shortcuts import render
from testimonials.models import Testimonial


def index(request):
    """ A view to render the home page """
    
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials,
    }

    return render(request, 'home/index.html', context)


# Privacy Policy 
def privacy_policy(request):
    """
    A view to render Privacy Policy page
    """

    context = {}
    return render(request, 'home/privacy_policy.html', context)

