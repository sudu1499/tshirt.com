from django.urls import path
from .views import individual
urlpatterns=[ 
    path('<product_id>/',individual)
]