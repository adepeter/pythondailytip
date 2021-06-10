from django import template

from ..models import PythonTipHashTag

register = template.Library()


@register.inclusion_tag('apps/twee/includes/templatetags/hash_tags.html', name='hashtags_template')
def hash_tags_with_template():
    tags = PythonTipHashTag.objects.all()
    return {'hash_tags': tags}


@register.simple_tag(name='hashtags')
def hash_tags_without():
    return PythonTipHashTag.objects.all()
