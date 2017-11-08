from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape as esc
import re

register = template.Library()

# Creating a template tag for highlighting a search term in search results
@register.filter(name='highlight')
def highlight(text, word):
    pattern = re.compile('{}'.format(esc(word)), re.IGNORECASE)
    return mark_safe(pattern.sub(r'<mark>{}</mark>'.format(word), text))
