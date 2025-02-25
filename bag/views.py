from django.shortcuts import render, redirect

# Create your views here.

def bag(request):
    """ A view to return the shopping bag """

    return render(request, 'bag/bag.html')

# view is a duplicate from Bourique Ado project from CodeInstitute tutorial , which is revised to suit this project.
def add_to_bag(request, item_id):
    """ Add a quantity of the specified service to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)