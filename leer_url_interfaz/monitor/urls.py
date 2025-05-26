from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import buscar_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check_changes, name='check'),
    path('done/', views.mark_all_checked, name='done'),
    path('reset/', views.reset_status, name='reset'),

    # nuevo codigo Alejandro 14/5/2025 se implementa codigo para guardar el check y que se quede guardado
    path('ajax/marcar/', views.marcar_checkbox_ajax, name='marcar_checkbox_ajax'),
    # nuevo codigo Alejandro 14/5/2025 se implementa codigo para guardar el check y que se quede guardado

    # nuevo codigo Alejandro 19/5/2025 se implementa codigo para guardar el check y que se quede guardado
    path('filtros/', views.filtros_genericos, name='filtros_genericos'),
    path('importar/', views.importar_archivo, name='importar_archivo'),
    path('exportar/', views.exportar_archivo, name='exportar_archivo'),
    # nuevo codigo Alejandro 19/5/2025 se implementa codigo para guardar el check y que se quede guardado
    
    # nuevo codigo Alejandro 19/5/2025 se implementa codigo para borrar importación
    path('reset_importacion/', views.reset_importacion, name='reset_importacion'),
    # nuevo codigo Alejandro 19/5/2025 se implementa codigo para borrar importación
    # nuevo codigo Alejandro 21/5/2025 se implementa codigo para crear filtro
    path('crear-filtro/', views.crear_filtro, name='crear_filtro'), 
    # nuevo codigo Alejandro 21/5/2025 se implementa codigo para crear filtro

    # nuevo código Doramas 22/5/2025 para editar el contenido y nombre de los filtros
    path('editar-filtro/<int:filtro_id>/', views.editar_filtro, name='editar_filtro'),
    # nuevo código Doramas 22/5/2025 para editar el contenido y nombre de los filtros
    # nuevo código Raúl 22/5/2025 para buscar urls
    path("buscar/", buscar_urls, name="buscar_urls"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
