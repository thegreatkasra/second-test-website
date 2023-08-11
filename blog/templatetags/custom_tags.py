from django import template
from django.utils.text import Truncator

register = template.Library()

#limit words in content of blog-home to 10 then ...

@register.filter
def limit_words_with_ellipsis(value, max_words):
    return Truncator(value).words(max_words, truncate=' ...')
