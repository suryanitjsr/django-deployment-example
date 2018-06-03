from django import template

register = template.Library()

@register.filter(name='remove')
def remove(value,arg):
    """
    This cuts out all vaue of args from string.
    """
    return value.replace(arg,'')
