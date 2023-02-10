from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
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

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
        'on_profile_page': True
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
            messages.success(request, 'Successfully updated product!')
            return redirect('/profile/')
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid')
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

# Add item to wishlist view 
@login_required(login_url='/accounts/login/')
def add_to_wishlist(request, id=None):
    """ 
    A view for user to add item to wishlist 
    """
    
    product = Product.objects.get(id=id)
    wish_item = None
    try:
        wish_item = WishList.objects.get(user=request.user, product=product)
    except WishList.DoesNotExist:
        wish_item = None
    if wish_item:
        wish_item.quantity += 1
        wish_item.save()
    else:
        wish_item = WishList.objects.create(user=request.user, product=product, quantity=1)
    return redirect('wishlist')

# Delete items from wishlist view 
@login_required(login_url='/accounts/login/')
def delete_from_wishlist(request, id=None):
    """ 
    A view for the user to delete item in wishlist 
    """
    
    product = Product.objects.get(id=id)
    wish_item = WishList.objects.get(user=request.user, product=product)
    wish_item.delete()
    return redirect('wishlist')