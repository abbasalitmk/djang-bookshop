from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Booktable


def user_login(request):
    message = ""
    if 'username' in request.session:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect('home')
        else:
            message = "Authentication failed!"
    return render(request, 'login-form.html', {'message': message})


def home(request):
    if 'username' in request.session:
        data = Booktable.objects.all()

        return render(request, 'home.html', {'data': data, 'current_user': request.session['username']})
    else:
        return redirect('login')


def signout(request):
    if 'username' in request.session:
        request.session.flush()
        return redirect('login')
