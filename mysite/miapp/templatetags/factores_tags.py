from django import template

register = template.Library()

@register.filter
def get_factor(factores, numero):
    return factores.filter(numero_factor=numero).first()

@register.filter
def to(value, end):
    return range(value, end + 1)
