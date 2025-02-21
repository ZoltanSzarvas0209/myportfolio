from django.shortcuts import render
from .models import Project

# Create your views here.

def portfolio(request):
    """ A view to show the portfolio page """
    return render(request, 'portfolio/portfolio.html')

def about(request):
    """ A view to show the about page """
    return render(request, 'portfolio/about.html')

def tech(request):
    """ A view to show the technologies page """
    return render(request, 'portfolio/tech.html')

def projects(request):
    """ A view to show the projects page """
    return render(request, 'portfolio/projects.html')