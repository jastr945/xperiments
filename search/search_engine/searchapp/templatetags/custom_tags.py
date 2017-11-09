from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

# Creating a custom template tag for highlighting matching search terms in search results

@register.filter(name='highlight')
def highlight(text, word):
    words_list = re.sub(r'[.!,;?]', ' ', word).split()
    text = r'{}'.format(text)
    replacement = "<mark>" + "\\1" + "</mark>"
    result = re.sub("(" + "|".join(map(re.escape, words_list)) + ")", replacement, text, flags=re.I)
    return mark_safe(result)
