from django.urls import path
from .views import index, home, phone, Description
from .import views

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('phone/', phone, name='phone'),
    path('Description/', Description, name='Description')
]