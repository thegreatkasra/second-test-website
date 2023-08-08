from django.urls import path    
from blog.views import blog_view ,blog_single
app_name = 'blog'

urlpatterns = [
    path('index_blog',blog_view, name='index_blog'),
    path('single',blog_single, name='single'),

]