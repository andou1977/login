from django.contrib import messages, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect

# Create your views here.
from login1.forms import formsdata
from login1.models import Test


def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f" Hello {username}, You Are Successfully Logged In")
            return render(request, "welcome.html")
        else:
            if not Test.objects.filter(username=username).exists():
                messages.error(request, "Username Doesn't Exist")
            else:
                messages.info(request, "Incorrect Password")
            return redirect('/')

    else:
        return render(request, "login.html")

# login reqired
@login_required
def register(request):
    password = 'PASSWORD_HERE'
    form = formsdata(request.POST or None)
    if form.is_valid():
        form.password = make_password(password)
        form.save()
        form = formsdata()
    return render(request, 'register.html', {'form': form})



@login_required
def admincool(request):
    return render(request, 'admin.html')

# login reqired
@login_required
def deconnection(request):
    logout(request)
    return redirect('login')


@login_required
def welcome(request):
    return render(request, 'welcome.html')


def logout_view(request):
    logout(request)
    return render(request, 'login.html')
    # Redirect to a success page.
