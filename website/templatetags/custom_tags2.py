from django import template
from blog.models import Post  


register = template.Library()

@register.inclusion_tag('slide-posts-index.html')
def slidshow():
    posts = Post.objects.filter(status=1).order_by('published_date')[:6]
    return {'posts': posts}
 