from django.shortcuts import render

# Create your views here.
def my_order(request):
    return render(request,'my_order.html')