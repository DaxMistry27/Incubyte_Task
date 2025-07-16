from django.shortcuts import render, redirect
from .forms import SweetForm

def add_sweet(request):
    if request.method == 'POST':
        form = SweetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_sweet')
    else:
        form = SweetForm()
    return render(request, 'shop/add_sweet.html', {'form': form})
