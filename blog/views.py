from django.shortcuts import render ,get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    #در view مربوط به لیست پست‌هایی که فیلتر صورت میگیرد چگونه می‌توان پست‌ها را مبتنی بر زمانی که برای published در نظر گرفته شده است فیلتر کرد. این فیلتر بایستی به گونه‌ای باشد که زمان در نظر گرفته شده برای بخش published_date را گرفته و با زمان حاضر مقایسه کند، اگر از زمان فعلی گذشته باشد می‌بایست نمایش داده شود و در غیر اینصورت خیر.
    current_time = timezone.now()  
    posts = Post.objects.filter(published_date__lte=current_time)
    context = {'posts':posts}
    return render(request,'blog-home.html',context)

def blog_single(request, pid):
    all_posts = Post.objects.all()
     #status=1 فقط به منتشر شده ها دسترسی نمایش میده
     #get_object_or_404 :  یعنی اگر نبود پیام 404 
    post = get_object_or_404(all_posts, pk=pid, status=1)
    #هر با دیده شود یکی اضافه کند
    post.counted_views += 1
    post.save()

    prev_post = all_posts.filter(pk__lt=pid).last()
    next_post = all_posts.filter(pk__gt=pid).first()
    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    return render(request,'blog-single.html',context)

