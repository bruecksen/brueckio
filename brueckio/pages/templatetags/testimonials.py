import datetime
from django import template

from pages.models import Testimonial

register = template.Library()

@register.simple_tag
def all_testimonials():
    return Testimonial.objects.filter(is_highlight=True).order_by('?')