from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import SignUpForm


def home_page(request):
    return render(request, 'home_page.html', {})


def user_signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/profile/')
        else:
            print(form.data, form.errors)
    else:
        return render(request, 'signup.html', {'form': form})
