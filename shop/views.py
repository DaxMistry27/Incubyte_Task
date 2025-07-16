from django.shortcuts import render, redirect,get_object_or_404

from .models import Sweet
from .forms import SweetForm

def add_sweet(request):
    if request.method == 'POST':
        form = SweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_sweet')
    else:
        form = SweetForm()
    
    sweets = Sweet.objects.all()
    return render(request, 'shop/add_sweet.html', {'form': form})

def delete_sweet(request, sweet_id):
    sweet = get_object_or_404(Sweet, id=sweet_id)
    if request.method == 'POST':
        sweet.delete()
        return redirect('add_sweet')
    return render(request, 'shop/confirm_delete.html', {'sweet': sweet})