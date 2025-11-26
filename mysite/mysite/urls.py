"""
URL configuration for mysite project.
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de documentación Swagger/Redoc
schema_view = get_schema_view(
    openapi.Info(
        title="API de Calificaciones",
        default_version='v1',
        description="Documentación de la API RESTful para Calificaciones y Factores",
        terms_of_service="https://www.tu-sitio.com/terms/",
        contact=openapi.Contact(email="soporte@tu-sitio.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Panel de administración
    path('admin/', admin.site.urls),

    # App principal
    path('', include('miapp.urls')),

    # Documentación automática de la API
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

from miapp.views_monitor import metrics_view

urlpatterns += [
    path("metrics/", metrics_view, name="metrics"),
]
