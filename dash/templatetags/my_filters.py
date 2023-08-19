from django import template

register = template.Library()

@register.filter
def get_class_name(value):
    return value.__class__.__name__

@register.filter
def get_field_label(form, field_name):
    return form[field_name].label
