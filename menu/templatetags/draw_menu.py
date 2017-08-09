from django import template
from menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(menu_name):
    nodes = MenuNode.objects.filter(belongs_to=menu_name)
    return {'nodes': nodes}
