from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import expenseForm

# Create your views here.


@login_required
def profile(request):
    return render(request, 'home.html', {})


@login_required
def add_category(request):
    form = expenseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            print(form)
        else:
            print(form.errors)
    return render(request, 'AddExpense.html', {'form': form})
