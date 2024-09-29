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

def description(request):
    return render(request, 'voltvibe/description.html')

def task_list(request):
    return render(request, 'voltvibe/list.html')
 