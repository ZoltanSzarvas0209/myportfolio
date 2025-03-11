from django.shortcuts import render, redirect, reverse
from django.http import JsonResponse
from django.contrib import messages
from services.models import Service


# Create your views here.

def bag(request):
    """ A view to return the shopping bag """

    return render(request, 'bag/bag.html')

# view is a duplicate from Bourique Ado project from CodeInstitute tutorial ,  was revised to suit this project.
def add_to_bag(request, item_id):
    """ Add a quantity of the specified service to the shopping bag """

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Succesfully adjusted quantity!')

    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {service.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    service = Service.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Succesfully adjusted quantity!')

    else:
        bag.pop(item_id)
        messages.success(request, f'Succesfully removed {service.name}!')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_from_bag(request, item_id):
    """Remove the specified item from the shopping bag"""

    service = Service.objects.get(pk=item_id)

    try:
        bag = request.session.get('bag', {})
        if str(item_id) in bag:
            del bag[str(item_id)]
            request.session['bag'] = bag
            messages.success(request, f'Succesfully removed {service.name}!')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Item not in bag'}, status=400)

    except Exception as e:
        messages.error(request, f'Error! The selected item was not removed!')
        return JsonResponse({'error': str(e)}, status=500)
