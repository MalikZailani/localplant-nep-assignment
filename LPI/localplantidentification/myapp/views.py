from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from form input
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Use email as username
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to dashboard after login
        else:
            return HttpResponse('Invalid email or password. Please try again.<a href="/login/">login</a>.')
    return render(request,"index.html")


@login_required
def dashboard(request):
    return render(request, 'Home Page.html')
    

def createaccount(request):
    #if request.user.is_authenticated:
     #       return redirect('home')
   

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
          # Redirect logged-in users

        # Check if the user already exists
        if User.objects.filter(email=email).exists():
            return HttpResponse('User already exists. Please <a href="/login/">login</a>.')

        # Create the new user
        user = User.objects.create_user(username=name, email=email, password=password)
        user.first_name = name  # Save full name in 'first_name'
        user.save()

        return redirect('index')  # Redirect to login after successful registration

    return render(request, 'create-account.html')  # Render the registration form

def forgotpassword(request):
    return render(request,"forgot-password.html")


def home(request):
    return render(request, "Home Page.html")


def notifications(request):
    return render(request, "Notification page.html") 


def settings(request):
    return render(request,"Setting page.html")

# Define route for the upload page

def upload(request):
    return render(request,"Upload Page.html")

def plantcommunity(request):
    return render(request,"Plant community page.html")

def result(request):
    return render(request,"Result Page.html")

# Define route for the user profile page



