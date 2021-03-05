from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


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
        error = False
        if len(User.objects.filter(username=username)) > 0:
            messages.error(request, 'نام کاربری شما در سیستم موجود است')
            error = True
        if password1 != password2:
            messages.error(request, 'گذرواژه و تکرار گذرواژه یکسان نیستند')
            error = True
        if error:
            return render(request, 'main/signup.html')
        else:
            user = User(username=username, email=email, first_name=firstname, last_name=lastname, is_active=True)
            user.set_password(password1)

            user.save()
            return render(request, 'main/index.html')

    else:
        return render(request, 'main/signup.html')


def login_page_view(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(request=request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'main/index.html')
        else:
            messages.error(request, "نام کاربری یا رمز عبور اشتباه است")
            return render(request, 'main/login.html')

    else:
        return render(request, 'main/login.html')


def logout_page_view(request):
    logout(request)
    return redirect('home')