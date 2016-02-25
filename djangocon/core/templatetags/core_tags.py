from django import template
from django.utils.safestring import mark_safe

from symposion.markdown_parser import parse

register = template.Library()

@register.filter
def markdown(text):
    return mark_safe(parse(text))


@register.filter
def sort_by_m2m(iterable, m2m_key):
    m2m, key = m2m_key.split('.')
    for i in iterable:
        keys = [getattr(related, key) for related in getattr(i, m2m).order_by(key)]

        i._key = ':'.join(keys)
    return sorted(iterable, key=lambda x: x._key)
