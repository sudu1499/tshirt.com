from django.contrib import admin

# # Register your models here.
from .models import checkout,order_payment_history,payement_order_sig
# buy_now_order
# admin.site.register(order)
admin.site.register(checkout)
# admin.site.register(buy_now_table)
admin.site.register(order_payment_history)
admin.site.register(payement_order_sig)