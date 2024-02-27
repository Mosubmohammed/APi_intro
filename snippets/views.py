from django.shortcuts import render
from .models import *

# Create your views here.

def TShirts(request):
    return render(request,'TShirts.html',{})