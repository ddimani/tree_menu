from django.urls import path
from .views import IndexPageView, MenuItemDetailView

app_name = 'menu_app'

urlpatterns = [
    path('', IndexPageView.as_view(), name='menu_display'),
    path(
        '<str:menu_name>/<path:item_path>/',
        MenuItemDetailView.as_view(),
        name='menu_item_detail'
    ),
]
