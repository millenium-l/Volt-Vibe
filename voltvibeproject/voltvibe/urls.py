from django.urls import path
from .views import index, account, home, phone, signin, signout
from .import views

urlpatterns = [
    path('index/', index, name='index'),
    path('account/', account, name='account'),
    path('home/', home, name='home'),
    path('phone/', phone, name='phone'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout')
]