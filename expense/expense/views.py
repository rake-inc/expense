from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                print(username, password)
                form.save(commit=True)
                print(form.data)
                return redirect('login')
            else:
                print(form.data)
        except Exception as e:
            print(e)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
