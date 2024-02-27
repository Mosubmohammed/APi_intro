from django.urls import path
from .views import *
urlpatterns = [
    path('',TShirts,name='Tshirt')
    
]