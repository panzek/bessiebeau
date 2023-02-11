from django.shortcuts import render
from testimonials.models import Testimonial
from profiles.models import UserProfile


def index(request):
    """ A view to render the home page """
    
    testimonials = Testimonial.objects.all()
    profile_image = UserProfile.objects.all()
    print(profile_image)

    context = {
        'testimonials': testimonials,
        'profile': profile_image,
    }

    return render(request, 'home/index.html', context)


# Privacy Policy 
def privacy_policy(request):
    """
    A view to render Privacy Policy page
    """

    context = {}

    return render(request, 'home/privacy_policy.html', context)


# Refund Policy 
def refund_policy(request):
    """
    A view to render Refund Policy page
    """

    context = {}

    return render(request, 'home/refund_policy.html', context)


# Terms of service  
def terms_of_service(request):
    """
    A view to render Terms of Service page
    """

    context = {}

    return render(request, 'home/terms_of_service.html', context)


# Delivery and Returns 
def delivery_returns(request):
    """
    A view to render Delivery and Returns page
    """

    context = {}

    return render(request, 'home/delivery_returns.html', context)


# How to Shop on Bessie + Beau 
def how_to_shop(request):
    """
    A view to render How to Shop on Bessie + Beau page
    """

    context = {}

    return render(request, 'home/how_to_shop.html', context)


# How to Shop on Bessie + Beau 
def user_guide(request):
    """
    A view to render user_guide page
    """

    context = {}

    return render(request, 'home/user_guide.html', context)