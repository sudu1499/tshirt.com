from django.db import models
from django.contrib.auth.models import User
from product_list.models import products
# Create your models here.
class cart(models.Model):
    user_name=models.ForeignKey(User,db_column='username',on_delete=models.DO_NOTHING)
    date_added=models.DateField(auto_now_add=True)
    product_id=models.ManyToManyField(products)
    product_count=models.IntegerField(default=1)
    size=models.CharField(max_length=50,default='')