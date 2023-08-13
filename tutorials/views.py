from django.shortcuts import render
from .models import Tutorials

def tutorials_me(request, *args, **kwargs):
    """
    Renders the Tutorials page
    """
    tutorials = Tutorials.objects.all().first()

    return render(
        request,
        "tutorials.html",
        {
            "tutorials": tutorials
        },
    )
