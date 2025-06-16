from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),  # Conecta las URLs de la app
    path('admin/', admin.site.urls),
]
