from django.urls import path
from .views import login_handler,signup_handler,logout_handler
urlpatterns=[ 
    path('login/',login_handler),
    path('signup/',signup_handler),
    path('logout/',logout_handler),
]