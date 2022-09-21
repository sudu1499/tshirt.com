from django.shortcuts import render
from .models import category
from django.conf import settings

###########
# from billing.models import checkout,order_payment_history
# # Create your views here.
# from Tshirt_cart.models import cart
def home(request):
    # obj=category()

    # obj1=cart.objects.all().delete()
    # obj1=checkout.objects.all().delete()
    # obj1=order_payment_history.objects.all().delete()

    context=category.objects.all()
    return render(request,'home.html',{'obj':context,'media_url':settings.MEDIA_URL})