from django import template
from blog.models import Category, Post


register = template.Library()


def get_all_categories():
    """Хешируемая фекция со всеми категориями"""
    return Category.objects.all()


@register.simple_tag()
def get_list_categories():
    """Вывод всех категорий"""
    return get_all_categories()


@register.inclusion_tag('include/tags/top_menu.html')
def get_categories():
    """Рендер панели с категориями"""
    category = get_all_categories()
    return {"list_category": category}


@register.inclusion_tag('include/tags/recipes_tag.html')
def get_last_posts():
    """Рендерит панель с новыми постами"""
    posts = Post.objects.select_related('category').order_by('-id')[:5]
    return {"list_last_post": posts}
