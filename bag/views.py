from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import JsonResponse


# Create your views here.

def bag(request):
    """ A view to return the shopping bag """

    return render(request, 'bag/bag.html')

# view is a duplicate from Bourique Ado project from CodeInstitute tutorial ,  was revised to suit this project.
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

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """Remove the specified item from the shopping bag"""
    try:
        bag = request.session.get('bag', {})
        if str(item_id) in bag:
            del bag[str(item_id)]
            request.session['bag'] = bag
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Item not in bag'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)