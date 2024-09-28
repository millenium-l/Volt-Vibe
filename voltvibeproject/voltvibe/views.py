from django.shortcuts import redirect, render
'''to store details to the database '''
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'voltvibe/index.html')

def home(request):
    return render(request, 'voltvibe/home.html')

def phone(request):
    return render(request, 'voltvibe/phone.html')

def Description(request):
    return render(request, 'voltvibe/Description.html')
 