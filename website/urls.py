from django.urls import path    
from website.views import index , contact , about

urlpatterns = [
    path('',index),
    path('contact',contact),
    path('about',about)
]