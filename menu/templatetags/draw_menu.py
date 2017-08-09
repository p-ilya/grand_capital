from itertools import chain
from django import template
from menu.models import MenuNode

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    nodes = MenuNode.objects.filter(belongs_to=menu_name).order_by('level')
    menu = build_tree(nodes)
    print(menu)
    return {'menu': menu}


def build_tree(nodes):
    menu = {}
    for node in nodes:
        children = [c for c in nodes if c.parent == node]
        if children:
            node.children = build_tree(children)
        print(list(chain.from_iterable(menu.values())))
        if node not in chain.from_iterable(menu.values()):
            menu[node] = children
    return menu
