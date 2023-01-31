from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile, User
from checkout.models import Order
from .forms import UserProfileForm
from products.models import Product
from profiles.models import WishList



@login_required(login_url='/accounts/login/')
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


@login_required(login_url='/accounts/login/')
def edit_profile(request, *args, **kwargs):
    """ A view to render edit user Profile page """
    userprofile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(
                request.POST, 
                request.FILES, 
                instance=userprofile
            )
        if form.is_valid:
            form.save()
            return redirect('/profile/')
    else:
        form = UserProfileForm(instance=userprofile)
    
    context = {
        'form': form
    }

    return render(request, 'profiles/edit_profile.html', context)


def delete_profile(request, *args, **kwargs):
    """ A view to render delete user Profile """
    
    userprofile = get_object_or_404(UserProfile, user=request.user)
    # u = User.objects.get(id=1)
    # u = User.objects.filter(username=userprofile) 
    userprofile.delete()

    return render(request, '')


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, 'checkout/checkout_success.html', context)

# Wishlist views 
@login_required(login_url='/accounts/login/')
def wishlist(request):
    """ A wishlist view """

    wish_items = WishList.objects.filter(user=request.user)
    context = {
        'wish_items': wish_items,
    }

    return render(request, 'profiles/wishlist.html', context)