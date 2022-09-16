from django.urls import path
from .views import list_cart,add_to_cart,update_db
urlpatterns=[ 
    path('list_cart/',list_cart),
    path('add_to_cart/',add_to_cart),
    path('update_db/',update_db)
]