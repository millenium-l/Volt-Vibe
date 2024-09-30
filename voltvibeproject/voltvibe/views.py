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


from django.shortcuts import get_object_or_404, redirect
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Get or create a cart for the user
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        # If it already exists, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the product page or wherever you prefer

def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'voltvibe/cart.html', {'cart': cart})


