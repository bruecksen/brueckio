from django import template
from django.template.loader import render_to_string

from wagtail.models import Site

register = template.Library()


@register.inclusion_tag('widgets/footer.html', takes_context=True)
def footer(context, *args, **kwargs):
    if 'request' in context:
        request = context['request']
        root_page = Site.find_for_request(request).root_page
        pages = root_page.get_children().filter(
            live=True,
            show_in_menus=True
        )
        return {
            'menu_items': pages,
            'request': context['request'],
            'page': 'page' in context and context['page'] or None,
        }


@register.inclusion_tag('widgets/header.html', takes_context=True)
def header(context, *args, **kwargs):
    if 'request' in context:
        request = context['request']
        root_page = Site.find_for_request(request).root_page
        pages = root_page.get_children().filter(
            live=True,
            show_in_menus=True
        )
        return {
            'menu_items': pages,
            'request': context['request'],
            'page': 'page' in context and context['page'] or None,
        }
