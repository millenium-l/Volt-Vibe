from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.http import HttpResponse
'''to store details to the database '''
from django.contrib.auth.models import User
'''to send messages after successfull login '''
from django.contrib import messages
''' to allow us to authenticate the user for login'''
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'voltvibe/index.html')

def account(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        '''to store details in the database '''
        myuser = User.objects.create_user(username, email, password)  

        myuser.save()

        messages.success(request, "your account has been successfully created.")

        return redirect('signin')


    return render(request, 'voltvibe/account.html')

def home(request):
    return render(request, 'voltvibe/home.html')

def phone(request):
    return render(request, 'voltvibe/phone.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']

        ''' django will authenticate the user to make sure it maches that of the database'''
        user = authenticate(username=username, password=password)

        ''' if the user has not created an acccount yet first he should '''
        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "voltvibe/home.html", {'username': username})

        else:
            messages.error(request, "Bad credentials!")
            return redirect('signin')


    return render(request, 'voltvibe/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "logged out successfully!")
    return redirect('signin')
 