from django.shortcuts import render
from .forms import ExpenseDetailsForm
from .models import ExpenseDetails
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
import requests
# Create your views here.


@login_required
def home_user(request):
    # print(dir(request))
    val = ExpenseDetails.objects.filter(owner_id=request.user).values()
    if len(val) == 0:
        val = 'none'
    else:
        data = serializers.serialize(
            'json', ExpenseDetails.objects.filter(owner_id=request.user),
            fields=('category', 'price', 'description'))
        requests.post(
            request.scheme + '://' +
            request.get_host() +
            request.get_full_path() +
            'json/',
            data=json.dumps(data),
            headers={'content-type': 'application/json'})

    return render(request, 'home_user.html', {'val': val})


@login_required
def home_add_details(request):
    form = ExpenseDetailsForm(None)
    if request.method == 'POST':
        form = ExpenseDetailsForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/profile/')
        else:
            print(form.errors)
    return render(request, 'home_add_details.html', {'form': form})


@login_required
def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/login')


@csrf_exempt
def get_json(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        return HttpResponse(data)
    else:
        return HttpResponse('none')
