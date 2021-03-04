from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from main.forms import UserForm


def home_page_view(request):
    return render(request, 'main/index.html')


def signup_page_view(request):
    if request.POST:
        form = UserForm(request.POST)
        if not form.is_valid():
            return HttpResponseBadRequest('not valid data')
        user = form.save()

        return redirect('home')
    else:
        data = {
            'form': UserForm()
        }
        return render(request, 'main/signup.html', data)
