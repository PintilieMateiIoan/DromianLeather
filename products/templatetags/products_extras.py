from django import template

register = template.Library()

@register.simple_tag
def subtractone(val):
    newval = val - 1
    return newval
