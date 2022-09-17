from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import cart
from product_list.models import products
from django.contrib.auth.models import User
from django.conf import settings
# Create your views here.
def list_cart(request):
    if request.user.is_authenticated:
        uuid=User.objects.get(username=request.user.username)
        print('got all object')
        print(uuid.id)
        cart_obj=cart.objects.filter(user_name=uuid.id)
        prod_obj=products.objects.all()
        for i in cart_obj:
            print(i.user_name)
        cart_prod=[]
        for i in cart_obj:
            cart_prod.append([i,products.objects.filter(id=i.product_id_id)[0]])
        return render(request,'cart.html',{'cart_prod':cart_prod,'media_url':settings.MEDIA_URL})

    else:
        return redirect('/validate/login/?next=/cart/')
    

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
        p=products.objects.filter(id=int(pid))[0]
        # obj1=cart.objects.get(product_id_id=int(pid),user_name=int(usn[0].id),size=size)
        try:
            obj1=cart.objects.get(product_id_id=int(pid),user_name=int(usn[0].id),size=size)
            if obj1.id:
                obj1.product_count+=int(pcnt)
                obj1.save()
            else:
                obj=cart.objects.create(user_name=usn[0],product_id_id=p.id,product_count=pcnt,size=size)
                obj.save()

        except:
            obj=cart.objects.create(user_name=usn[0],product_id_id=p.id,product_count=pcnt,size=size)
        # obj.product_id.set(pid)
            obj.save()
        print('done')
        # obj.user_name=username
        # obj.product_id=pid
        # obj.product_count=pcnt
        # obj.size=size
        return render(request,'cart.html')

    else:
        return render(request,'cart.html')


def update_db(request):
    print('got some values from ajax',request.GET)
    obj=cart.objects.get(id=int(request.GET['id']))
    obj.product_count=int(request.GET['updated_count'])
    obj.save()
    print('updated')
    return JsonResponse({'message':request.GET['updated_count']})

def delete_item(request):
    print('command to delete an item')
    obj=cart.objects.get(id=int(request.GET['cart_id']))
    obj.delete()
    print('deleted')
    return JsonResponse({'message': 'deleted record'})

