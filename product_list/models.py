from django.db import models
from home.models import category
# Create your models here.

class products(models.Model):

    product_id=models.IntegerField()
    product_name=models.CharField(max_length=50)
    brand=models.CharField(max_length=50,default='')
    descriptions=models.CharField(max_length=50)
    price=models.FloatField()
    count=models.IntegerField()
    size_s=models.IntegerField(default=0)
    size_m=models.IntegerField(default=0)
    size_l=models.IntegerField(default=0)
    size_xl=models.IntegerField(default=0)
    size_xxl=models.IntegerField(default=0)
    category=models.ForeignKey(category,on_delete=models.DO_NOTHING)
    discount=models.FloatField(default=0)
    colour=models.CharField(max_length=50,default='')
    img=models.ImageField(upload_to='product_list/images',default='')
    rating=models.FloatField(null=True)

    def __str__(self):
        return self.product_name