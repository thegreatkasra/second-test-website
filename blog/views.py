from django.shortcuts import render ,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator  import Paginator ,EmptyPage ,PageNotAnInteger

def blog_view(request,author_username=None,**kwargs):
    #در view مربوط به لیست پست‌هایی که فیلتر صورت میگیرد چگونه می‌توان پست‌ها را مبتنی بر زمانی که برای published در نظر گرفته شده است فیلتر کرد. این فیلتر بایستی به گونه‌ای باشد که زمان در نظر گرفته شده برای بخش published_date را گرفته و با زمان حاضر مقایسه کند، اگر از زمان فعلی گذشته باشد می‌بایست نمایش داده شود و در غیر اینصورت خیر.
    current_time = timezone.now()  
    posts = Post.objects.filter(published_date__lte=current_time,status=1).order_by('published_date')
    if author_username:
        posts = posts.filter(author__username=author_username)
    if kwargs.get('tag_name') != None:
        posts = Post.filter(tag__name__in =[kwargs['tag_name']])

    #Pagination(next-previous page)
    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts}
    return render(request,'blog-home.html',context)
    

def blog_single(request, pid):
    current_time = timezone.now() 
    all_posts = Post.objects.all()
     #status=1 فقط به منتشر شده ها دسترسی نمایش میده
     #get_object_or_404 :  یعنی اگر نبود پیام 404 
    post = get_object_or_404(all_posts, pk=pid, status=1 ,published_date__lte=current_time)
    #هر با دیده شود یکی اضافه کند
    post.counted_views += 1
    post.save()

    prev_post = all_posts.filter(pk__lt=pid,status=1).last()
    next_post = all_posts.filter(pk__gt=pid,status=1).first()
    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request,'blog-single.html',context)

#make url for categories
def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request,'categories-posts.html',context)

#SEARCH function
def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains = request.GET.get('s'))
    context = {'posts':posts}
    return render(request,'blog-home.html',context)



