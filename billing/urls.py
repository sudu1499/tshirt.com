from django.urls import path
from .views import add_to_checkout,order_success,create_razorpay_order,buy_now
# ,buy_now
urlpatterns=[ 
    path('add_to_order/',add_to_checkout),
    path('success/<username>/<buy_now>/',order_success),
    path('create_razorpay_order/',create_razorpay_order),
    path('buy_now/',buy_now),
]