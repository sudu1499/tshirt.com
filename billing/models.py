from django.db import models
from Tshirt_cart.models import cart
from django.contrib.auth.models import User
from product_list.models import products
# Create your models here.
class checkout(models.Model):
    # id as order id
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    date=models.DateField(auto_now_add=True)
    product_id=models.ForeignKey(products,on_delete=models.DO_NOTHING)
    order_count=models.IntegerField(default=1)
    # order_count=models.ForeignKey(cart,db_column='product_count',on_delete=models.CASCADE)
    # price_of_one=models.ForeignKey(products,db_column='price',on_delete=models.CASCADE,related_name='cost_of_one')
    price_of_one=models.FloatField(default=1)
    total_amount=models.FloatField(default=0)

class order_payment_history(models.Model):

    order_id=models.AutoField(primary_key=True)###########changed
    prod_id=models.ForeignKey(products,on_delete=models.DO_NOTHING)##########new
    count=models.IntegerField(default=1)###########new
    user=models.ForeignKey(User,db_column='username',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField()
    status=models.CharField(max_length=50,default='')
    payment_order_id=models.CharField(max_length=100,default='')

class payement_order_sig(models.Model):

    user=models.CharField(max_length=100)
    razorpay_payment_id=models.CharField(max_length=100)
    razorpay_order_id=models.CharField(max_length=100)
    razorpay_signature=models.CharField(max_length=100)
    buy_now=models.CharField(max_length=10)


# class buy_now_table(models.Model):
#     # id as order id
#     user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
#     date=models.DateField(auto_now_add=True)
#     product_id=models.ForeignKey(products,on_delete=models.DO_NOTHING)
#     order_count=models.IntegerField(default=1)
#     # order_count=models.ForeignKey(cart,db_column='product_count',on_delete=models.CASCADE)
#     # price_of_one=models.ForeignKey(products,db_column='price',on_delete=models.CASCADE,related_name='cost_of_one')
#     price_of_one=models.FloatField(default=1)
#     total_amount=models.FloatField(default=0)

# payement_order_sig.objects.create(user=username,razorpay_payment_id=raz_payment_id
#             ,razorpay_order_id=raz_order_id,razorpay_signature=raz_sig,buy_now=buy_now)