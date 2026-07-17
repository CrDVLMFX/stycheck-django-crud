from django.contrib import admin
from django.urls import path, include
# 1. Importamos la vista de redirección
from django.views.generic import RedirectView

urlpatterns = [
    # 2. Esta línea mágica redirige la página principal vacía a /servicios/
    path('', RedirectView.as_view(url='servicios/', permanent=True)),
    
    path('admin/', admin.site.urls),
    path('servicios/', include('servicios.urls')), # O como tengas configurada tu app de servicios
]