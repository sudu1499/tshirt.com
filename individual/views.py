from django.shortcuts import render
from product_list.models import products
from django.conf import settings
# Create your views here.
def individual(request,product_id):
    print('product id is ',product_id)
    obj=products.objects.filter(id=int(product_id))
    print("#######",len(obj))
        
    return render(request,'individual.html',{'obj':obj[0],'media_url':settings.MEDIA_URL,'session':request.session})