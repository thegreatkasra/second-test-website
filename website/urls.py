from django.urls import path    
from website.views import index , contact , about , element , Newsletter_view
app_name = 'website'

urlpatterns = [
    path('',index , name='index'),
    path('contact',contact , name='contact'),
    path('about',about , name='about'),
    path('element',element , name='elements'),
    path('newsletter', Newsletter_view , name='newsletter'),
]