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




#
# asgiref==3.6.0
# beautifulsoup4==4.11.1
# certifi==2022.12.7
# charset-normalizer==3.0.1
# click==8.1.3
# colorama==0.4.6
# contourpy==1.0.7
# cycler==0.11.0
# Django==4.1.6
# django-bootstrap-v5==1.0.11
# django-bootstrap5==22.2
# django-embed-video==1.4.8
# django-filter==22.1
# django-forms-bootstrap==3.1.0
# django-mysql==4.8.0
# django-settings==1.3.12
# django_debug_toolbar==3.8.1
# djangorestframework==3.14.0
# filterpy==1.4.5
# Flask==2.2.2
# fonttools==4.38.0
# form==0.0.1
# idna==3.4
# itsdangerous==2.1.2
# Jinja2==3.1.2
# kiwisolver==1.4.4
# MarkupSafe==2.1.2
# matplotlib==3.6.3
# msgpack==1.0.4
# mysqlclient==2.1.1
# numpy==1.24.1
# packaging==23.0
# Pillow==9.4.0
# psycopg2-binary==2.9.5
# pyparsing==3.0.9
# pyping==0.0.6
# python-dateutil==2.8.2
# pytz==2022.7.1
# requests==2.28.2
# scipy==1.10.0
# six==1.16.0
# soupsieve==2.3.2.post1
# sqlparse==0.4.3
# tzdata==2022.7
# urllib3==1.26.14
# Werkzeug==2.2.2
