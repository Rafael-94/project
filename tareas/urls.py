from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/crear/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:tarea_id>/', views.ver_tarea, name='ver_tarea'),
    path('tareas/<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:tarea_id>/borrar/', views.borrar_tarea, name='borrar_tarea'),
]
