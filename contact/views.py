from django.shortcuts import render
from .models import Contact

def contact_me(request, *args, **kwargs):
    """
    Renders the Contact page
    """
    contact = Contact.objects.all().first()

    return render(
        request,
        "contact.html",
        {
            "contact": contact
        },
    )
