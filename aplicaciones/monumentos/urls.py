from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
urlpatterns = [
    path('', views.inicio, name='inicio'),
    # vistas de plantillas
    path('listado_encargado', views.listado_encargado, name='listado_encargado'),
    path('listado_materiales', views.listado_materiales, name='listado_materiales'),
    path('listado_monumentos', views.listado_monumentos, name='listado_monumentos'),
    path('listado_proyectos', views.listado_proyecto, name='listado_proyectos'),
    #agregar datos en las plantillas
    path('agregar_encargado', views.agregar_encargado, name='agregar_encargado'),
    path('agregar_materiales', views.agregarmateriales, name='agregar_materiales'),
    path('agregar_monumentos', views.agregar_monumento, name='agregar_monumentos'),
    path('agregar_proyectos', views.agregar_proyecto, name='agregar_proyectos'),
    #ediar datos en las plantillas
    path('editar_encargado/<int:id>/', views.editarencargado, name='editar_encargado'),
    path('editar_materiales/<int:id>/', views.editarmateriales, name='editar_materiales'),
    path('editar_monumentos/<int:id>/', views.editarmonumento, name='editar_monumentos'),
    path('editar_proyectos/<int:id>/', views.editarproyecto, name='editar_proyectos'),
    
    # eliminar datos en las plantillas
    path('eliminar_encargado/<int:id>/', views.eliminarencargado, name='eliminar_encargado'),
    path('eliminar_materiales/<int:id>/', views.eliminarmateriales, name='eliminar_materiales'),
    path('eliminar_monumentos/<int:id>/', views.eliminarmonumentos, name='eliminar_monumentos'),
    path('eliminar_proyectos/<int:id>/', views.eliminarproyectos, name='eliminar_proyectos'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
