from django.urls import path
from .views import my_order

urlpatterns=[ 
    path('',my_order)
]