from django.shortcuts import render
from blog.models import Post

def blog_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'blog-home.html',context)

def blog_single(request):
    return render(request,'blog-single.html')



