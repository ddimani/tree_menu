from django.views.generic import TemplateView

from .models import MenuItem


class IndexPageView(TemplateView):
    template_name = "index.html"


class MenuItemDetailView(TemplateView):
    model = MenuItem
    template_name = "menu_item_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["item_path"] = self.kwargs["item_path"]
        return context
