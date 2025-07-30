import debug_toolbar
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend_menu import settings

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('menu_app.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
