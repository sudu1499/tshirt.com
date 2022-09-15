from django.urls import path
from .views import *

urlpatterns=[ 
    path('<category_name>/',product_list)
]