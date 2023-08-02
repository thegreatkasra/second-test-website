from django.urls import path    
from website.views import index , contact , about , element
app_name = 'website'

urlpatterns = [
    path('',index , name='index'),
    path('contact',contact , name='contact'),
    path('about',about , name='about'),
    path('element',element , name='element')
]