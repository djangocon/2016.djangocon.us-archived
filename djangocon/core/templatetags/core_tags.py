from django import template


register = template.Library()


@register.filter
def sort_by_m2m(iterable, m2m_key):
    m2m, key = m2m_key.split('.')
    for i in iterable:
        keys = [str(getattr(related, key)) for related in getattr(i, m2m).order_by(key)]

        i._key = ':'.join(keys)
    return sorted(iterable, key=lambda x: x._key)
