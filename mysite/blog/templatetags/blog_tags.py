from django import template
from ..models import Post
<<<<<<< HEAD
from django.db.models import Count
from django.utils.safestring import mark_safe
import markdown
=======
>>>>>>> be8bda85bcc865affa2b67d8e65a6c9ffd05e4d7


register = template.Library()


<<<<<<< HEAD
@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]

=======
@register.simple_tag
def total_posts():
    return Post.published.count()
>>>>>>> be8bda85bcc865affa2b67d8e65a6c9ffd05e4d7
