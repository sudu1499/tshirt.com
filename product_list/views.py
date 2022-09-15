import imp
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import products
from home.models import category
from django.conf import settings

# Create your views here.
def product_list(request,category_name):
    print('in product list')
    c=category.objects.get(category_name=category_name)
    obj=products.objects.all().filter(category_id=c.id)
    for i in obj:
        print(i.rating)
    return render(request,'product_list.html',{'obj':obj,'media_url':settings.MEDIA_URL,'media_root':settings.MEDIA_ROOT,'category_name':category_name})

