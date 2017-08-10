from django import template
from menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    nodes = MenuNode.objects.filter(belongs_to=menu_name).filter(level=0)
    return {'nodes': nodes}
