from django.shortcuts import redirect, render
'''to store details to the database '''
from django.contrib.auth.models import User
from .models import Product

from .forms import ProductCreateForm

# Create your views here.
def index(request):
    return render(request, 'voltvibe/index.html')

def cart(request):
    return render(request, 'voltvibe/cart.html')

def home(request):
    return render(request, 'voltvibe/home.html')

def phone(request):
    return render(request, 'voltvibe/phone.html')

def description(request):
    return render(request, 'voltvibe/description.html')

def product(request):
    product = Product.objects.all()
    return render(request, 'voltvibe/product.html', {'product':product})
 
# we are creating our view form for product cart
def Product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    # if form method is not post the user can refresh    
    else:
        form = ProductCreateForm()

    return render(request, 'voltvibe/create.html', {'form':form})
