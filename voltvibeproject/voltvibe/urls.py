from django.urls import path
from .views import index, style

urlpatterns = [
    path('index/', index, name='index'),
]