from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


def edit_profile(request):
    """ A view to render edit user Profile page """

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid:
            profile = form.save(commit=False)
            profile.email = request.user.email
            profile.username = request.user.username
            profile.save()
    else:
        form = UserProfileForm()
    
    context = {
        'form': form
    }

    return render(request, 'profiles/edit_profile.html', context)