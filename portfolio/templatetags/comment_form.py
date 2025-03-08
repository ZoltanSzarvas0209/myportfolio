# the template tag is created using ChatGPT - fix for issue with rendering form
from django import template

register = template.Library()


@register.filter
def dictkey(dictionary, key):
    """Retrieve a value from a dictionary using a key in Django templates."""
    return dictionary.get(key, "")
