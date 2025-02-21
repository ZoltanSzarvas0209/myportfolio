from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    """ A view to show all services available """

    return render(request, 'portfolio/portfolio.html')