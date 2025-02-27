from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import Contact_form


def contact(request):
    """
    Render the contact page with the contact form.

    **Context**

    - `contactform`: An instance of the contactForm class.

    **Template:**

    template:`contact.html`
    """
    if request.method == "POST":
        contactform = Contact_form(data=request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.info(request, f'Thank you for your message, I will get back to you as soon as possible!')

    contactform = Contact_form()

    return render(
        request,
        "contact/contact.html",
        {
            "contactform": contactform
        },
    )