from django import template
register = template.Library()


@register.filter
def word_count(value):
    return len(value.split())

@register.simple_tag()
def greet_user(value):
    return f'Hello {value}!'


def upper_case(value):
    return value.upper() if isinstance(value, str) else value