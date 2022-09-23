from django.shortcuts import render
from billing.models import order_payment_history
from django.contrib.auth.models import User
from product_list.models import products
from tshirt.settings import MEDIA_URL
# Create your views here.
def my_order(request):
    user_obj=User.objects.get(username=request.user.username)
    my_order_obj=order_payment_history.objects.filter(user=user_obj.id)
    order_prod=[]
    for i in my_order_obj:
        prod_obj=products.objects.get(id=i.prod_id_id)
        order_prod.append([i,prod_obj])
    

    return render(request,'my_order.html',{'order_prod':order_prod,'MEDIA_URL':MEDIA_URL})