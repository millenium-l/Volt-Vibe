from django.urls import path
from .views import index, home, phone, description
from .import views

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('phone/', phone, name='phone'),
    path('description/', description, name='description')
]