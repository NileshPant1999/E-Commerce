from django.urls import path
from .views import products, CheckOut


app_name = 'core'

urlpatterns = [
   path('', products, name='products'),
   path('checkout', CheckOut, name='checkout'),
]