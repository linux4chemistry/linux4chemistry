from django import template
from django.conf import settings
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(needs_autoescape=True)
def license_img(value, autoescape=None):
    """return the img element for the license"""
    images = {
        'Open Source': 'img/opensource.png',
        'Freeware': 'img/freeware.png',
        'Free for academics': 'img/academic.png',
        'Shareware': 'img/shareware.png',
        'Commercial': 'img/commercial.png',
        }

    esc = conditional_escape if autoescape else lambda x: x
    element = '&nbsp;<img src="{0}{{0}}"/>'.format(esc(settings.STATIC_URL))

    name = value.name
    output = element.format(esc(images[name])) if name in images else ''
    return mark_safe(output)

