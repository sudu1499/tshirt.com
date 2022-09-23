from django.urls import path
from .views import add_to_checkout,order_success,create_razorpay_order,buy_now,payment_status, unload_f
# ,buy_now
urlpatterns=[ 
    path('add_to_order/',add_to_checkout),
    path('success/<username>/<buy_now>/',order_success),
    path('success/order_success/',order_success),
    path('status/<status>/',payment_status),
    path('create_razorpay_order/',create_razorpay_order),
    path('buy_now/',buy_now),
    path('unload/',unload_f),
]