from .models import Contact
from django import forms


class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('title', 'content')