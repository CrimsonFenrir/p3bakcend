from django.urls import path, include
from . import views
from .views_api import CalificacionViewSet, CalificacionFactorViewSet
from rest_framework import routers
from django.shortcuts import redirect

# Router de DRF para la API RESTful
router = routers.DefaultRouter()
router.register(r'calificaciones', CalificacionViewSet)
router.register(r'factores', CalificacionFactorViewSet)

def root_redirect(request):
    return redirect('login')

urlpatterns = [
    # Redirige la raíz al login
    path('', root_redirect),

    # Autenticación
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # CRUD Calificaciones (protegidas)
    path('calificaciones/', views.lista_calificaciones, name='lista_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/<int:id_calificacion>/editar/', views.actualizar_calificacion, name='actualizar_calificacion'),
    path('calificaciones/<int:id_calificacion>/eliminar/', views.eliminar_calificacion, name='eliminar_calificacion'),

    # Importar Excel
    path('calificaciones/importar/', views.importar_calificaciones, name='importar_calificaciones'),

    # API JSON básica (legacy)
    path('api/calificaciones/json/', views.api_calificaciones, name='api_calificaciones'),

    # API RESTful completa con DRF
    path('api/', include(router.urls)),
]
