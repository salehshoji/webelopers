from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect

from main.forms import UserForm


def home_page_view(request):
    return render(request, 'main/index.html')


def signup_page_view(request):
    if request.POST:
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if len(User.objects.filter(username=username)) > 0:
            messages.error(request, 'نام کاربری شما در سیستم موجود است')
            return redirect('signup-page')
        if password1 != password2:
            messages.error(request, 'گذرواژه و تکرار گذرواژه یکسان نیستند')
            return redirect('signup-page')

        user = User(username=username, email=email, first_name=firstname, last_name=lastname, is_active=True)
        user.set_password(password1)

        user.save()
        return redirect('home')
    else:
        data = {
            'form': UserForm()
        }
        return render(request, 'main/signup.html', data)
