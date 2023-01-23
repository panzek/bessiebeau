from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


@login_required(login_url='/accounts/login/')
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'profile': profile,
    }

    return render(request, 'profiles/profile.html', context)


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    """ A view to render edit user Profile page """

    if request.method == 'POST':
        form = UserProfileForm(
                request.POST, 
                request.FILES, 
                instance=request.user.userprofile
            )
        if form.is_valid:
            form.save()
            return redirect('/profile/')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    context = {
        'form': form
    }

    return render(request, 'profiles/edit_profile.html', context)