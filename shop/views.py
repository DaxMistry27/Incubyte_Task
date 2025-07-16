from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import Sweet
from .forms import SweetForm

def add_sweet(request):
    form = SweetForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('add_sweet')

    # Filtering logic
    sweets = Sweet.objects.all()

    # Search by name
    search = request.GET.get('search')
    if search:
        sweets = sweets.filter(name__icontains=search)

    # Filter by category
    category = request.GET.get('category')
    if category and category != 'All':
        sweets = sweets.filter(category=category)

    # Price range
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        sweets = sweets.filter(price__gte=min_price)
    if max_price:
        sweets = sweets.filter(price__lte=max_price)

    # Sort
    sort = request.GET.get('sort')
    if sort in ['name', 'price', 'quantity']:
        sweets = sweets.order_by(sort)

    return render(request, 'shop/add_sweet.html', {
        'form': form,
        'sweets': sweets,
    })


def delete_sweet(request, sweet_id):
    sweet = get_object_or_404(Sweet, id=sweet_id)
    if request.method == 'POST':
        sweet.delete()
        return redirect('add_sweet')
    return render(request, 'shop/confirm_delete.html', {'sweet': sweet})

def purchase_sweet(request):
    sweets = Sweet.objects.all()
    error = None

    if request.method == 'POST':
        sweet_id = request.POST.get('sweet_id')
        quantity = int(request.POST.get('quantity', 0))
        sweet = get_object_or_404(Sweet, id=sweet_id)

        if sweet.quantity >= quantity:
            sweet.quantity -= quantity
            sweet.save()
            return redirect('add_sweet')
        else:
            error = "Not enough stock"

    return render(request, 'shop/purchase_sweet.html', {
        'sweets': sweets,
        'error': error
    })