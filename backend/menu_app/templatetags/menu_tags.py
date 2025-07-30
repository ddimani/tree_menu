from collections import defaultdict
from django import template
from django.urls import reverse
from django.utils.safestring import mark_safe
from menu_app.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    item_path = context.get('item_path')
    path_slugs = item_path.strip('/').split('/') if item_path else []

    items = list(
        MenuItem.objects.select_related('parent', 'menu')
        .filter(menu__name=menu_name)
    )

    parent_map = {item.id: item.parent for item in items}

    children_map = defaultdict(list)
    for item in items:
        children_map[item.parent_id].append(item)

    active_items = []
    current_parent = None

    for slug in path_slugs:
        match = next(
            (item for item in children_map[current_parent] if item.slug == slug
             ),
            None
        )
        if not match:
            break
        active_items.append(match)
        current_parent = match.id

    def get_url(item):
        slugs = []
        current = item
        while current:
            slugs.append(current.slug)
            current = parent_map.get(current.id)
        full_path = '/'.join(reversed(slugs))
        return reverse('menu_app:menu_item_detail', kwargs={
            'menu_name': item.menu.name,
            'item_path': full_path
        })

    def render(parent_id=None):
        html = '<ul>'
        for item in children_map.get(parent_id, []):
            is_expanded = item in active_items
            class_attr = ' class="expanded"' if is_expanded else ''
            html += (
                f'<li{class_attr}><a '
                f'href="{get_url(item)}">{item.title}</a>'
            )
            if is_expanded and children_map.get(item.id):
                html += render(item.id)
            html += '</li>'
        html += '</ul>'
        return html

    return mark_safe(render())
