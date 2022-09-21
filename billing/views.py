from ast import Delete
import hashlib
from re import T
from django.http import HttpResponse
from pydoc import cli
from django.shortcuts import render
from Tshirt_cart.models import cart
from .models import order,payment_history,buy_now_order
from product_list.models import products
from django.contrib.auth.models import User
import razorpay
from tshirt.settings import RAZORPAY_SECRET_KEY,RAZORPAY_KEY_ID
from django.views.decorators.csrf import csrf_exempt
import hmac
import json
def add_to_order(request):
    uuid=User.objects.get(username=request.user.username)
    cart_obj=cart.objects.filter(user_name=uuid.id)
    for i in cart_obj:
        order_count=i.product_count
        prod_obj=products.objects.get(id=i.product_id_id)
        price_of_one=prod_obj.price
        total_sum=order_count*price_of_one
        print('order_count',order_count,'price_of_one',price_of_one)
        print('total to be paid',total_sum)
        try:
            ob=order.objects.get(user=uuid,product_id_id=prod_obj)
            if ob:
                if ob.order_count==i.product_count:
                    print('already there')
                else:
                    print('count is different')
                    ob.order_count=i
                    ob.total_amount=total_sum
                    ob.save()
        except:
            print('in except')
            order_obj=order.objects.create(user=uuid,product_id_id=prod_obj.id,
            order_count=i,price_of_one=prod_obj.price,total_amount=total_sum)
            order_obj.save()
    ob=order.objects.filter(user=uuid)
    total_sum=0
    cart_order_prod=[]
    for i in ob:
        cart_order_prod.append([cart.objects.get(product_id_id=i.product_id_id,user_name=uuid),i,products.objects.get(id=i.product_id_id)])  
        total_sum+=i.total_amount
    print(cart_order_prod)

    client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_SECRET_KEY))
    data={
        'amount':total_sum,
        'currency':'INR',
        'receipt':'#1','payment_capture':True}
    payment=client.order.create(data=data)
    print('order id is ',payment['id'])
    checkout_obj=payment_history.objects.create(user=request.user,amount=total_sum,order_id=payment['id'])
    checkout_obj.save()
    print('checkout_obj created')

    return render(request,'buy.html',{'cart_order_prod':cart_order_prod,'total_sum':total_sum,'total_sum_paise':total_sum*100,
    'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID,'payment':payment,'buy_now':False})
@csrf_exempt
def order_success(request):
    if request.POST:
        if 'razorpay_payment_id' in request.POST:
            raz_payment_id=request.POST['razorpay_payment_id']
            raz_order_id=request.POST['razorpay_order_id']
            raz_sig=request.POST['razorpay_signature']
            msg=raz_order_id+"|"+raz_payment_id
            gs=hmac.new(str.encode(RAZORPAY_SECRET_KEY),msg.encode('UTF-8'),hashlib.sha256)
            generated_sig=gs.hexdigest()
            client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_SECRET_KEY))
            if raz_sig==generated_sig:
                obj=payment_history.objects.get(order_id=raz_order_id)
                obj.status='sucessfull'
                obj.save()
                print('sucessfull status saved')
                cart.objects.all().delete()
                try:
                    buy_now_order.objects.all().delete()
                except:
                    pass

                client.utility.verify_payment_signature({
                    'razorpay_order_id': raz_order_id,
                    'razorpay_payment_id': raz_payment_id,
                    'razorpay_signature': raz_sig})
                return render(request,'status.html',{'status':'Thank u We got your order'})
            else:
                obj=payment_history.objects.get(order_id=raz_order_id)
                obj.status='failure'
                obj.save()
                print('failure status saved')
                return HttpResponse('no')
        else:
                d=request.POST['error[metadata]']
                oid=json.loads(d)['order_id']
                print(oid)
                obj=payment_history.objects.get(order_id=oid)
                obj.status='failure'
                obj.save()
                return render(request,'status.html',{'status':'Sorry we didnot get ur order'})

    return HttpResponse('bad request')

def buy_now(request):
    if request.POST:
        prod_obj=products.objects.get(id=int(request.POST['product_id']))
        total_sum=int(request.POST['count'])*prod_obj.price
        obj=buy_now_order.objects.create(user=request.user,product_id=prod_obj,order_count=request.POST['count'],
        price_of_one=prod_obj.price,total_amount=total_sum)

        client=razorpay.Client(auth=(RAZORPAY_KEY_ID,RAZORPAY_SECRET_KEY))
        data={
        'amount':total_sum,
        'currency':'INR',
        'receipt':'#1','payment_capture':True}
        payment=client.order.create(data=data)
        print('order id is ',payment['id'])
        checkout_obj=payment_history.objects.create(user=request.user,amount=total_sum,order_id=payment['id'])
        checkout_obj.save()
        print('checkout_obj created')
        return render(request,'buy.html',{'buy_now':True,'total_sum':total_sum,'total_sum_paise':total_sum*100,
    'RAZORPAY_KEY_ID':RAZORPAY_KEY_ID,'payment':payment,'prod_obj':prod_obj,'count':request.POST['count']})
    