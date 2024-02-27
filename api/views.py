from django.shortcuts import render

# Create your views here.

from rest_framework import generic
from snippets.models import *   
from .serializers import BookSerializer

class TShirts(generic.ListAPIView):
    queryset=Clothes.objects.all()
    serializer_class=BookSerializer
    


