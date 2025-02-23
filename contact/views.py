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
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for getting in touch,\
                we will respond as soon as possible!"
            )

    contactform = Contact_form()

    return render(
        request,
        "contact/contact.html",
        {
            "contactform": contactform
        },
    )