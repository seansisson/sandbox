from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    """
    Returns hello world to the template
    """
    greeting = "Hello world"

    return render(request, 'dash/home.html', {
        "greeting": greeting,
    })
