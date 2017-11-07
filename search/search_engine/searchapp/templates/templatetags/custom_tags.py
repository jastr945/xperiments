from django import template


register = template.Library()

# Creating a template tag for highlighting a search term in search results
@register.filter(name='highlight')
def highlight(text):
    
