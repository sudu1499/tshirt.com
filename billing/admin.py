from django.contrib import admin

# Register your models here.
from .models import order,payment_history,buy_now_order
admin.site.register(order)
admin.site.register(payment_history)
admin.site.register(buy_now_order)