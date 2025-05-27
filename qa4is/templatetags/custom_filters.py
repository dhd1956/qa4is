from django import template

register = template.Library()

@register.filter
def getattribute(obj, attribute):
    return getattr(obj, attribute)

