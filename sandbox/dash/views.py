from django.shortcuts import render

def home():
    """
    Returns hello world to the template
    """
    greeting = "Hello world"

    return render(request, 'dash/home.html', {
        "greeting": greeting,
    })
