from django.urls import path
from .views import index, home, phone, description, product, Product_create, add_to_cart, view_cart
from .import views

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('phone/', phone, name='phone'),
    path('description/', description, name='description'),
    path('product/', product, name='product'),
    path('create/', Product_create, name='create'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart')
]

urlpatterns += [
    path('cart/', view_cart, name='view_cart'),
]
