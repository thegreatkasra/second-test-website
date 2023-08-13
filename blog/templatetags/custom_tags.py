from django import template
from django.utils.text import Truncator
from blog.models import Post
 

register = template.Library()

#limit words in content of "blog-home" to 10 then ...

@register.filter
def limit_words_with_ellipsis(value, max_words):
    return Truncator(value).words(max_words, truncate=' ...')

#ما را به جایی ارجاع میده که آخرین پست ها کش میشوند
@register.inclusion_tag('latest-posts.html')
def latestpost(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}