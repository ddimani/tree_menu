from django.contrib import admin

from .models import MenuItem, Menu


class MenuItemAdmin(admin.ModelAdmin):
    """Настройки административной панели для модели MenuItem."""

    list_display = ('title', 'slug', 'parent')
    list_filter = ('title',)
    search_fields = ('title', 'slug',)
    ordering = ('title', 'id')


class MenuAdmin(admin.ModelAdmin):
    """Настройки административной панели для модели MenuItem."""

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Menu, MenuAdmin)
