from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def time_since(value):
    now = timezone.now()
    diff = now - value

    if diff.days > 0:
        return f'{diff.days}일 전'
    elif diff.seconds > 3600:
        return f'{diff.seconds // 3600}시간 전'
    elif diff.seconds > 60:
        return f'{diff.seconds // 60}분 전'
    else:
        return '방금 전'
