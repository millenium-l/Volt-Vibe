from django.urls import path
from .views import index, home, phone, description, product, Product_create
from .import views

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('phone/', phone, name='phone'),
    path('description/', description, name='description'),
    path('product/', product, name='product'),
    path('create/', Product_create, name='create')
]