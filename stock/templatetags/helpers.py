from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag
def link_to(name, url, *args):
    name = template.Variable(name)

    if (len(args) > 0 and str(args[-1]).startswith('attrs:')):
        args, attrs = args[:-1], args[-1]
    else:
        args, attrs = args, ''

    url = reverse(url, args=tuple(args))
    attrs = attrs.replace('attrs:', '')

    return '<a href="{1}" {2}>{0}</a>'.format(name, url, attrs)

