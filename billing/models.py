from django.db import models
from Tshirt_cart.models import cart
from django.contrib.auth.models import User
from product_list.models import products
# Create your models here.
class order(models.Model):
    # id as order id
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    product_id=models.ForeignKey(products,on_delete=models.CASCADE)
    order_count=models.ForeignKey(cart,db_column='product_count',on_delete=models.CASCADE,related_name='number_of_prducts')
    # price_of_one=models.ForeignKey(products,db_column='price',on_delete=models.CASCADE,related_name='cost_of_one')
    price_of_one=models.FloatField(default=1)
    total_amount=models.FloatField(default=0)

class payment_history(models.Model):

    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User,db_column='username',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    amount=models.FloatField()
    status=models.CharField(max_length=50,default='')
    order_id=models.CharField(max_length=100,default='')

class buy_now_order(models.Model):
    # id as order id
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    product_id=models.ForeignKey(products,on_delete=models.CASCADE)
    order_count=models.IntegerField(default=1)
    # price_of_one=models.ForeignKey(products,db_column='price',on_delete=models.CASCADE,related_name='cost_of_one')
    price_of_one=models.FloatField(default=1)
    total_amount=models.FloatField(default=0)