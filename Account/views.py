from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home_name')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home_name')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'نام کاربری یا رمز عبور اشتباه است'})
    else:
        return render(request, 'login.html')
