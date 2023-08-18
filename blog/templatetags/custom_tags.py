from django import template
from django.utils.text import Truncator
from blog.models import Post
from blog.models import Category
 

register = template.Library()

#limit words in content of "blog-home" to 10 then ...

@register.filter
def limit_words_with_ellipsis(value, max_words):
    return Truncator(value).words(max_words, truncate=' ...')

#ما را به جایی ارجاع میده که آخرین پست ها کش میشوند
#sidebar lastposts widget
@register.inclusion_tag('latest-posts.html')
def latestpost(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

#اضافه کردن ساید بار کتگوری
#add categories widget sidebar
@register.inclusion_tag('categories-posts.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}

#search bar widget
@register.inclusion_tag('blog-search.html')
def search_bar():
    return {}
