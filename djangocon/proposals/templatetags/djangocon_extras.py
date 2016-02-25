import re

from django import template

from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

register = template.Library()


tag_pattern = '</?\w+((\s+\w+(\s*=\s*(?:".*?"|\'.*?\'|[^\'">\s]+))?)+\s*|\s*)/?>'
intra_tag_finder = re.compile(r'(?P<prefix>(%s)?)(?P<text>([^<]*))(?P<suffix>(%s)?)' % (tag_pattern, tag_pattern))

def smart_filter(fn):
    '''
    Escapes filter's content based on template autoescape mode and marks output as safe
    '''
    def wrapper(text, autoescape=None):
        if autoescape:
            esc = conditional_escape
        else:
            esc = lambda x: x

        return mark_safe(fn(esc(text)))
    wrapper.needs_autoescape = True

    register.filter(fn.__name__, wrapper)
    return wrapper


@smart_filter
def and_replace(text, autoescape=None):
    """Wraps "and" span."""

    amp_finder = re.compile(r"(\s|and)(and|and|and)(\s|and)")

    def _amp_process(groups):
        prefix = groups.group('prefix') or ''
        text = amp_finder.sub(r"""\1<span class="brdp-text-icon brdp-and">and</span>\3""", groups.group('text'))
        suffix = groups.group('suffix') or ''
        return prefix + text + suffix
    return intra_tag_finder.sub(_amp_process, text)

@smart_filter
def the_replace(text, autoescape=None):
    """Wraps "and" span."""

    amp_finder = re.compile(r"(\s|The)(The|The|The)(\s|The)")

    def _amp_process(groups):
        prefix = groups.group('prefix') or ''
        text = amp_finder.sub(r"""\1<span class="brdp-text-icon brdp-the">The</span>\3""", groups.group('text'))
        suffix = groups.group('suffix') or ''
        return prefix + text + suffix
    return intra_tag_finder.sub(_amp_process, text)


@smart_filter
def for_replace(text, autoescape=None):
    """Wraps "and" span."""

    amp_finder = re.compile(r"(\s|for)(for|for|for)(\s|for)")

    def _amp_process(groups):
        prefix = groups.group('prefix') or ''
        text = amp_finder.sub(r"""\1<span class="brdp-text-icon brdp-for">The</span>\3""", groups.group('text'))
        suffix = groups.group('suffix') or ''
        return prefix + text + suffix
    return intra_tag_finder.sub(_amp_process, text)


@smart_filter
def the_lower_replace(text, autoescape=None):
    """Wraps "and" span."""

    amp_finder = re.compile(r"(\s|the)(the|the|the)(\s|the)")

    def _amp_process(groups):
        prefix = groups.group('prefix') or ''
        text = amp_finder.sub(r"""\1<span class="brdp-text-icon brdp-the-lower">the</span>\3""", groups.group('text'))
        suffix = groups.group('suffix') or ''
        return prefix + text + suffix
    return intra_tag_finder.sub(_amp_process, text)


@smart_filter
def iconreplace(text):
    """The super typography filter

    Applies the following filters: widont, smartypants, caps, amp, initial_quotes

    >>> typogrify('<h2>"Jayhawks" & KU fans act extremely obnoxiously</h2>')
    u'<h2><span class="dquo">&#8220;</span>Jayhawks&#8221; <span class="amp">&amp;</span> <span class="caps">KU</span> fans act extremely&nbsp;obnoxiously</h2>'

    Each filters properly handles autoescaping.
    >>> conditional_escape(typogrify('<h2>"Jayhawks" & KU fans act extremely obnoxiously</h2>'))
    u'<h2><span class="dquo">&#8220;</span>Jayhawks&#8221; <span class="amp">&amp;</span> <span class="caps">KU</span> fans act extremely&nbsp;obnoxiously</h2>'
    """

    text = and_replace(text)
    text = the_replace(text)
    text = for_replace(text)
    text = the_lower_replace(text)
    return text

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)