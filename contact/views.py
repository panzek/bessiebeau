from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    A view to render form in template
    """

    form = ContactForm(request.POST)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()

            messages.success(request, 'Contact form was successfully submitted')
            return redirect('home')
        else:
            messages.error(request, 'Failed to submit contact form. Please ensure the form is valid')
    else:
        form = ContactForm()

        template = 'contact/contact.html'
        context = {
            'form': form,
        }

    return render(request, template, context)

