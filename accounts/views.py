from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def login(request):
    if request.method == 'POST':
        print("login_test")
        messages.error(request, 'Testing Error Message')
        return redirect('register')

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    return redirect(request, 'index')

def register(request):
    if request.method == 'POST':
        # Form Data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_match = request.POST['password_match']

        # Check password
        if password != password_match:
            messages.error(request, 'Passwords do not match')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request,'This username is taken')
            
            return redirect('register')
 
        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is being used')

            return redirect('register')
           

        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name,
                )
            user.save()
            messages.success(request, 'You are now registered')
            return redirect('login')
            # login after registered
            # auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            # return redirect('index')
           
    else:
        return render(request, 'accounts/register.html')