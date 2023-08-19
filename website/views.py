from django.shortcuts import render
from blog.models import Post


def index(request):
    latest_posts = Post.objects.order_by('-published_date')[:6]

    context = {'posts': latest_posts}
    return render(request,'index.html',context)

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def element(request):
    return render(request,'element.html')

#6 posts slidshow in index.html