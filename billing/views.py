import hashlib
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from Tshirt_cart.models import cart
from .models import checkout,order_payment_history
from product_list.models import products
from django.contrib.auth.models import User
import razorpay
from tshirt.settings import RAZORPAY_SECRET_KEY,RAZORPAY_KEY_ID
from django.views.decorators.csrf import csrf_exempt
import hmac
import json

def unload_f(request):
    print('got unload command',request)
    # uuid=User.objects.get(username=request.user.username)
    # checkout.objects.filter(user=uuid).delete()
    return JsonResponse({'msg':'unloaded'})

def add_to_checkout(request):
    uuid=User.objects.get(username=request.user.username)
    cart_obj=cart.objects.filter(user_name=uuid.id)
    checkout.objects.filter(user=uuid).delete()
    for i in cart_obj:
        order_count=i.product_count
        prod_obj=products.objects.get(id=i.product_id_id)
        price_of_one=prod_obj.price
        total_sum=order_count*price_of_one
        print('order_count',order_count,'price_of_one',price_of_one)
        print('total to be paid',total_sum)
        try:
            ob=checkout.objects.get(user=uuid,product_id_id=prod_obj)
            if ob:
                if ob.order_count==i.product_count:
                    print('already there')
                else:
                    print('count is different')
                    ob.order_count=i.product_count
                    ob.total_amount=total_sum
                    ob.save()
        except:
            print('in except')
            # checkout.objects.filter(user=uuid.id).delete()
            order_obj=checkout.objects.create(user=uuid,product_id_id=prod_obj.id,
            order_count=i.product_count,price_of_one=prod_obj.price,total_amount=total_sum)
            order_obj.save()
    ob=checkout.objects.filter(user=uuid)
    total_sum=0
    cart_order_prod=[]
    print('hello bhai')
    for i in ob:
        cart_order_prod.append([cart.objects.get(product_id_id=i.product_id_id,user_name=uuid.id),i,products.objects.get(id=i.product_id_id)])  
        total_sum+=i.total_amount
    print(cart_order_prod)

    return render(request,'buy.html',{'cart_order_prod':cart_order_prod,'total_sum':total_sum,'total_sum_paise':total_sum*100,
    'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID,'buy_now':False})

@csrf_exempt
def order_success(request,username,buy_now):
    if request.POST:
        if 'razorpay_payment_id' in request.POST:
            print("aaaa",username)
            uuid=User.objects.get(username=username)
            ckt_obj=checkout.objects.filter(user_id=uuid.id)
            print(uuid,uuid.id)

            raz_payment_id=request.POST['razorpay_payment_id']
            raz_order_id=request.POST['razorpay_order_id']
            raz_sig=request.POST['razorpay_signature']
            msg=raz_order_id+"|"+raz_payment_id
            gs=hmac.new(str.encode(RAZORPAY_SECRET_KEY),msg.encode('UTF-8'),hashlib.sha256)
            generated_sig=gs.hexdigest()
            client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_SECRET_KEY))
            print('comming')
            if raz_sig==generated_sig:
                for i in ckt_obj:
                    prd_obj=products.objects.get(id=i.product_id_id)
                    obj=order_payment_history.objects.create(prod_id_id=prd_obj.id,count=i.order_count,user=uuid,amount=i.total_amount,status='success',
                    payment_order_id=raz_order_id)
                    obj.save()
                print('sucessfull status saved')
                if buy_now=='False':
                    cart.objects.filter(user_name=uuid.id).delete()
                checkout.objects.filter(user=uuid.id).delete()
                client.utility.verify_payment_signature({
                    'razorpay_order_id': raz_order_id,
                    'razorpay_payment_id': raz_payment_id,
                    'razorpay_signature': raz_sig})

                return redirect('/buy/status/1/')
            else:
                for i in ckt_obj:
                    prd_obj=products.objects.get(id=i.product_id_id)
                    obj=order_payment_history.objects.create(prod_id_id=prd_obj.id,count=i.order_count,user=uuid,amount=i.total_amount,status='failure',
                    payment_order_id=raz_order_id)
                    obj.save()
                print('failure status saved')
                return redirect('/buy/status/0/')
        else:
                print(request)
                d=request.POST['error[metadata]']
                print(d)
                oid=json.loads(d)['order_id']
                print(oid)
                for i in ckt_obj:
                    prd_obj=products.objects.get(id=i.product_id_id)
                    obj=order_payment_history.objects.create(prod_id_id=prd_obj.id,count=i.order_count,user=uuid,amount=i.total_amount,status='failure',
                    payment_order_id=oid)
                    obj.save()
                obj.save()
                return redirect('/buy/status/0/')


    return HttpResponse('bad request')
def payment_status(request,status):
    if int(status)==1:
        msg='Thank u we got ur order'
    else:
        msg='Sorry we didnot get ur order'
    return render(request,'status.html',{'status':msg})

def create_razorpay_order(request):
        uuid=User.objects.get(username=request.user.username)
        ckt_obj=checkout.objects.filter(user_id=uuid.id)
        total_sum=0
        for i in ckt_obj:
            total_sum+=i.total_amount
        client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_SECRET_KEY))
        data={
            'amount':float(total_sum)*100,
            'currency':'INR',
            'receipt':'#1','payment_capture':True}
        payment=client.order.create(data=data)
        print('in ajax order id is ',payment['id'])
        return JsonResponse({'payment_id':payment['id'],'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID})


def buy_now(request):
    if request.POST:
        print(request.user)
        print('in buy now')
        prod_obj=products.objects.get(id=int(request.POST['product_id']))
        uuid=User.objects.get(username=request.user.username)
        checkout.objects.filter(user=uuid).delete()

        # try:
        #     ckt_obj=checkout.objects.filter()
        checkout_obj=checkout.objects.create(user=uuid,product_id_id=request.POST['product_id'],order_count=request.POST['count'],
        price_of_one=request.POST['product_price'],total_amount=int(request.POST['count'])*float(request.POST['product_price']))
        checkout_obj.save()

        return render(request,'buy.html',{'prod_obj':prod_obj,'total_sum':int(request.POST['count'])*float(request.POST['product_price']),
        'total_sum_paise':int(request.POST['count'])*float(request.POST['product_price'])*100,'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID,'buy_now':True,'count':request.POST['count']})





    	