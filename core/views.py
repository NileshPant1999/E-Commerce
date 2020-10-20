from django.shortcuts import render
from .models import Item
from rest_framework import generics
# Create your views here.

def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'products.html', context)

def CheckOut(request):
    return render(request, 'checkout.html')

def home(request):
    context = {
        'items': Item.objects.all()
    }

    return render(request, "home.html", context)

from .serializers import ItemSerializer



# API CBVS

class ItemListAPIView(generics.ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer