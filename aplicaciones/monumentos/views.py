from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')


########################################################################################################################################
# Vistas de las diferentes plantillas

# Vista encargado

def listado_encargado(request):
    encargado = Encargado.objects.all()
    return render(request, 'listado_encargado.html', {'encargado': encargado})

# Vista materiales

def listado_materiales(request):
    materiales = Materiales.objects.all()
    return render(request, 'listado_materiales.html', {'materiales': materiales})

# Vista monumentos

def listado_monumentos(request):
    monumentos = Monumento.objects.all()
    return render(request, 'listado_monumentos.html', {'monumentos': monumentos})

# Vista proyectos

def listado_proyecto(request):
    proyectos = Proyecto.objects.all()
    monumentos = Monumento.objects.all()
    return render(request, 'listado_proyectos.html', {
        'proyectos': proyectos,
        'monumentos': monumentos
    })


########################################################################################################################################
# agregar de las diferentes plantillas

# agregar de encargado

def agregar_encargado(request):
    if request.method == 'POST':
        nombre = request.POST['txt_nombre']
        cargo = request.POST['txt_cargo']
        telefono = request.POST['txt_telefono']
        correo = request.POST['txt_correo']
        nuevoEncargado = Encargado.objects.create(
            nombre=nombre,
            cargo=cargo,
            telefono=telefono,
            correo=correo
        )
        messages.success(request, "Encargado agregado exitosamente.")
        return redirect('listado_encargado')
    return render(request, "agregar_encargado.html")


# agregar de materiales

def agregarmateriales(request):
    if request.method == 'POST':
        nombre = request.POST['txt_nombre']
        descripcion = request.POST.get('txt_descripcion', '')
        cantidad_disponible = request.POST['txt_cantidad']

        nuevo_material = Materiales.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            cantidad_disponible=cantidad_disponible
        )
        messages.success(request, "Material agregado exitosamente.")
        return redirect('listado_materiales')

    return render(request, "agregar_materiales.html")

# agregar de monumentos

def agregar_monumento(request):
    if request.method == 'POST':
        nombre = request.POST['txt_nombre']
        ubicacion = request.POST['txt_ubicacion']
        descripcion = request.POST.get('txt_descripcion', '')
        fecha_construccion = request.POST['txt_fecha_construccion']
        foto = request.FILES.get("txt_foto")

        nuevo_monumento = Monumento.objects.create(
            nombre=nombre,
            ubicacion=ubicacion,
            descripcion=descripcion,
            fecha_construccion=fecha_construccion,
            foto=foto
        )
        messages.success(request, "Monumento agregado exitosamente.")
        return redirect('listado_monumentos')

    return render(request, "agregar_monumentos.html")

# agregar de proyectos

def agregar_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST['txt_nombre']
        descripcion = request.POST['txt_descripcion']
        fecha_inicio = request.POST['txt_fecha_inicio']
        fecha_fin_estimada = request.POST['txt_fecha_fin_estimada']
        monumento_id = request.POST['txt_monumento']
        encargado_id = request.POST.get('txt_encargado')
        materiales_ids = request.POST.getlist('txt_materiales')
        foto = request.FILES.get("txt_foto")

        # Obtener instancias de los modelos relacionados
        monumento = Monumento.objects.get(id=monumento_id)
        encargado = Encargado.objects.get(id=encargado_id) if encargado_id else None
        materiales = Materiales.objects.filter(id__in=materiales_ids)

        # Crear el proyecto
        nuevo_proyecto = Proyecto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            fecha_inicio=fecha_inicio,
            fecha_fin_estimada=fecha_fin_estimada,
            monumento=monumento,
            encargado=encargado,
            foto=foto
        )

        # Asignar los materiales al proyecto
        nuevo_proyecto.materiales.set(materiales)

        messages.success(request, "Proyecto agregado exitosamente.")
        return redirect('listado_proyectos')

    # Obtener datos para el formulario
    monumentos = Monumento.objects.all()
    encargados = Encargado.objects.all()
    materiales = Materiales.objects.all()

    return render(request, "agregar_proyectos.html", {
        "monumentos": monumentos,
        "encargados": encargados,
        "materiales": materiales
    })

########################################################################################################################################
# editar de las diferentes plantillas

# editar encargado

def editarencargado(request, id):
    encargado = get_object_or_404(Encargado, id=id)

    if request.method == 'POST':
        encargado.nombre = request.POST.get('txt_nombre')
        encargado.cargo = request.POST.get('txt_cargo')
        encargado.telefono = request.POST.get('txt_telefono')
        encargado.correo = request.POST.get('txt_correo')
        encargado.save()
        messages.success(request, "Encargado actualizado exitosamente.")
        return redirect('listado_encargado')

    return render(request, 'actualizar_encargado.html', {'encargado': encargado})

# editar materiales

def editarmateriales(request, id):
    material = get_object_or_404(Materiales, id=id)

    if request.method == 'POST':
        material.nombre = request.POST.get('txt_nombre')
        material.descripcion = request.POST.get('txt_descripcion', '')
        material.cantidad_disponible = request.POST.get('txt_cantidad')
        material.save()
        messages.success(request, "Material actualizado exitosamente.")
        return redirect('listado_materiales')

    return render(request, 'actualizar_materiales.html', {'material': material})

# editar monumentos

def editarmonumento(request, id):
    monumento = get_object_or_404(Monumento, id=id)

    if request.method == 'POST':
        monumento.nombre = request.POST.get('txt_nombre')
        monumento.ubicacion = request.POST.get('txt_ubicacion')
        monumento.descripcion = request.POST.get('txt_descripcion')
        monumento.fecha_construccion = request.POST.get('txt_fecha_construccion')
        monumento.save()
        messages.success(request, "Monumento actualizado exitosamente.")
        return redirect('listado_monumentos')

    return render(request, 'actualizar_monumentos.html', {'monumento': monumento})

# editar proyectos

def editarproyecto(request, id):
    proyecto = get_object_or_404(Proyecto, id=id)
    monumentos = Monumento.objects.all()
    encargados = Encargado.objects.all()
    materiales = Materiales.objects.all()

    if request.method == 'POST':
        proyecto.nombre = request.POST.get('txt_nombre')
        proyecto.descripcion = request.POST.get('txt_descripcion')
        proyecto.fecha_inicio = request.POST.get('txt_fecha_inicio')
        proyecto.fecha_fin_estimada = request.POST.get('txt_fecha_fin_estimada')

        # Asignar Monumento
        monumento_id = request.POST.get('txt_monumento')
        if monumento_id:
            proyecto.monumento = get_object_or_404(Monumento, id=monumento_id)

        # Asignar Encargado
        encargado_id = request.POST.get('txt_encargado')
        if encargado_id:
            proyecto.encargado = get_object_or_404(Encargado, id=encargado_id)

        # Asignar Materiales (ManyToMany)
        materiales_ids = request.POST.getlist('txt_materiales')
        proyecto.materiales.set(Materiales.objects.filter(id__in=materiales_ids))

        proyecto.save()
        messages.success(request, "Proyecto actualizado exitosamente.")
        return redirect('listado_proyectos')

    return render(request, 'actualizar_proyectos.html', {
        'proyecto': proyecto,
        'monumentos': monumentos,
        'encargados': encargados,
        'materiales': materiales
    })


########################################################################################################################################
# eliminar de las diferentes plantillas

# Eliminar encargado

def eliminarencargado(request, id):
    encargado = Encargado.objects.get(id=id)
    encargado.delete()
    messages.success(request, "Encargado eliminado exitosamente.")
    return redirect('listado_encargado')

# eliminar materiales

def eliminarmateriales(request, id):
    materiales = Materiales.objects.get(id=id)
    materiales.delete()
    messages.success(request, "Material eliminado exitosamente.")
    return redirect('listado_materiales')

# eliminar monumentos

def eliminarmonumentos(request, id):
    monumentos = Monumento.objects.get(id=id)
    monumentos.delete()
    messages.success(request, "Monumento eliminado exitosamente.")
    return redirect('listado_monumentos')

# eliminar proyectos

def eliminarproyectos(request, id):
    proyectos = Proyecto.objects.get(id=id)
    proyectos.delete()
    messages.success(request, "Proyecto eliminado exitosamente.")
    return redirect('listado_proyectos')
