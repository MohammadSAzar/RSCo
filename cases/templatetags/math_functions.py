from django import template

register = template.Library()

@register.filter
def mul_func(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1*num2

