from django.shortcuts import render
from .models import category
from django.conf import settings
# Create your views here.
def home(request):
    # obj=category()
    context=category.objects.all()
    return render(request,'home.html',{'obj':context,'media_url':settings.MEDIA_URL})