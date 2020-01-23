from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.inclusion_tag('widgets/footer.html', takes_context=True)
def footer(context, *args, **kwargs):
    request = context['request']
    root_page = context['request'].site.root_page
    pages = root_page.get_children().filter(
        live=True,
        show_in_menus=True
    )
    return {
        'menu_items': pages,
        'request': context['request'],
        'page': context['page'],
    }


@register.inclusion_tag('widgets/header.html', takes_context=True)
def header(context, *args, **kwargs):
    request = context['request']
    root_page = context['request'].site.root_page
    pages = root_page.get_children().filter(
        live=True,
        show_in_menus=True
    )
    return {
        'menu_items': pages,
        'request': context['request'],
        'page': context['page'],
    }
