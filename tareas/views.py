from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

def index(request):
    # Esta función muestra la página de inicio
    return render(request, 'index.html')

def lista_tareas(request):
    # Esta función muestra la lista de todas las tareas
    tareas = Tarea.objects.all()  # Obtenemos todas las tareas de la base de datos
    return render(request, 'lista_tareas.html', {'tareas': tareas})  # Renderizamos la plantilla lista_tareas.html y pasamos las tareas como contexto

def crear_tarea(request):
    # Esta función permite crear una nueva tarea
    if request.method == 'POST':
        # Si la solicitud es de tipo POST, significa que se envió un formulario
        form = TareaForm(request.POST)  # Creamos un formulario con los datos de la solicitud
        if form.is_valid():
            # Si el formulario es válido, guardamos la nueva tarea en la base de datos
            form.save()
            return redirect('lista_tareas')  # Redirigimos al usuario a la lista de tareas
    else:
        # Si la solicitud no es de tipo POST, mostramos un formulario vacío
        form = TareaForm()
    return render(request, 'crear_tarea.html', {'form': form})  # Renderizamos la plantilla crear_tarea.html y pasamos el formulario como contexto

def ver_tarea(request, tarea_id):
    # Esta función muestra los detalles de una tarea específica
    tarea = Tarea.objects.get(pk=tarea_id)  # Obtenemos la tarea correspondiente al ID proporcionado
    return render(request, 'ver_tarea.html', {'tarea': tarea})  # Renderizamos la plantilla ver_tarea.html y pasamos la tarea como contexto

def editar_tarea(request, tarea_id):
    # Esta función permite editar una tarea existente
    tarea = Tarea.objects.get(pk=tarea_id)  # Obtenemos la tarea correspondiente al ID proporcionado
    if request.method == 'POST':
        # Si la solicitud es de tipo POST, significa que se envió un formulario con los datos actualizados
        form = TareaForm(request.POST, instance=tarea)  # Creamos un formulario con los datos de la solicitud y la instancia de la tarea a editar
        if form.is_valid():
            # Si el formulario es válido, guardamos los cambios en la tarea
            form.save()
            return redirect('ver_tarea', tarea_id=tarea_id)  # Redirigimos al usuario a la página de detalles de la tarea
    else:
        # Si la solicitud no es de tipo POST, mostramos un formulario prellenado con los datos de la tarea
        form = TareaForm(instance=tarea)
    return render(request, 'editar_tarea.html', {'form': form})  # Renderizamos la plantilla editar_tarea.html y pasamos el formulario como contexto

def borrar_tarea(request, tarea_id):
    # Esta función permite eliminar una tarea existente
    tarea = Tarea.objects.get(pk=tarea_id)  # Obtenemos la tarea correspondiente al ID proporcionado
    if request.method == 'POST':
        # Si la solicitud es de tipo POST, significa que se confirmó la eliminación de la tarea
        tarea.delete()  # Eliminamos la tarea de la base de datos
        return redirect('lista_tareas')  # Redirigimos al usuario a la lista de tareas
    return render(request, 'borrar_tarea.html', {'tarea': tarea})  # Renderizamos la plantilla borrar_tarea.html y pasamos la tarea como contexto
