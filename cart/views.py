from django.shortcuts import render,HttpResponse,redirect
from .models import cart
from product_list.models import products
from django.contrib.auth.models import User
# Create your views here.
def cart_f(request):
    if request.user.is_authenticated:
        return render(request,'cart.html')
    else:
        return redirect('/validate/login/?next=/cart/')\
    

def add_to_cart(request):
    if request.POST:
        print("username=",request.user.username)
        print("product_id=",request.POST['product_id'])
        print("size=",request.POST['size'])
        print("coubnt=",request.POST['count'])
        username=request.user.username
        pid=request.POST['product_id']
        size=request.POST['size']
        pcnt=request.POST['count']
        usn=User.objects.all().filter(username=username)
        # print(usn[0].username)
        obj=cart.objects.create(user_name=usn[0],product_count=pcnt,size=size)
        obj.product_id.set(pid)
        obj.save()
        print('done')
        # obj.user_name=username
        # obj.product_id=pid
        # obj.product_count=pcnt
        # obj.size=size
        return render(request,'cart.html')

    else:
        return render(request,'cart.html')
