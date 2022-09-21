from django.contrib import admin

# # Register your models here.
from .models import checkout,order_payment_history
# buy_now_order
# admin.site.register(order)
admin.site.register(checkout)
admin.site.register(order_payment_history)
# admin.site.register(buy_now_order)