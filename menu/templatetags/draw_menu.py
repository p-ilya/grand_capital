from django import template
from menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    max_level = context['page'].level + 1
    nodes = MenuNode.objects.filter(belongs_to=menu_name).filter(level=0)
    return {'nodes': nodes, 'active': context['page'], 'max_level': max_level}
