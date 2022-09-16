from django import template

register=template.Library()

@register.simple_tag
def int_f(value):
    return int(value)