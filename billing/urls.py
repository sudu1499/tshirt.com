from django.urls import path
from .views import add_to_order,order_success,buy_now
urlpatterns=[ 
    path('add_to_order/',add_to_order),
    path('success/',order_success),
    path('buy_now/',buy_now),
]