from django.urls import path    
from blog.views import blog_view ,blog_single

app_name = 'blog'

urlpatterns = [
    path('in',blog_view, name='in'),
    path('single',blog_single, name='single'),

]