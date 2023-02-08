from django.shortcuts import render


def handle_404(request, exception):
    """
    A view to render HTTP 404 errors page
    """

    context = {}

    return render(request, '404.html', context)