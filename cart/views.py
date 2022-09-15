from django.shortcuts import render,HttpResponse,redirect
from .models import cart
from product_list.models import products
# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        return render(request,'cart.html')
    else:
        return redirect('/validate/login/?next=/cart/')\
    

def add_to_cart(request):
    if request.POST:
        # print("$$$$",request.POST['product_id'])
        # pid=products.objects.get(id=request.POST['product_id'])
        # print(pid)
        print('request.user.username ',request.user.username)
        print("request.POST['product_id'] ",request.POST['product_id'])
        obj=Cart.objects.create(cart_id=request.POST['product_id'],user_name=request.user.username)
        # obj.cart_id=request.POST['product_id']
        # obj.user_name=request.user.username
        obj.save()
        print('added ')
        return render(request,'cart.html')

    else:
        return render(request,'cart.html')
