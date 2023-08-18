from django.urls import path    
from blog.views import blog_view ,blog_single, blog_category

app_name = 'blog'

urlpatterns = [
    path('',blog_view, name='index_blog'),
    path('<int:pid>',blog_single, name='single'),
    path('category/<str:cat_name>',blog_category , name='category'),
    path('author/<str:author_username>',blog_view, name = 'author'),
]