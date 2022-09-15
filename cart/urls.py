from django.urls import path
from .views import cart,add_to_cart
urlpatterns=[ 
    path('list_cart/',cart),
    path('add_to_cart/',add_to_cart),
]