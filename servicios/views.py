from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServicioForm
from .models import Servicio


def listar_servicios(request):
    """
    GET: muestra el catálogo completo, con filtro opcional por
    categoría (RF09) y paginación de 10 registros por página.
    """
    servicios_list = Servicio.objects.all()

    categoria = request.GET.get('categoria')
    if categoria:
        servicios_list = servicios_list.filter(categoria=categoria)

    paginator = Paginator(servicios_list, 10)
    pagina = request.GET.get('page')
    servicios = paginator.get_page(pagina)

    return render(
        request,
        'servicios/lista.html',
        {
            'servicios': servicios,
            'categorias': Servicio.CATEGORIA_CHOICES,
            'categoria_actual': categoria,
        },
    )


def crear_servicio(request):
    """
    GET: muestra el formulario vacío.
    POST: valida y guarda un nuevo servicio.
    """
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio creado correctamente.')
            return redirect('listar_servicios')
    else:
        form = ServicioForm()

    return render(
        request,
        'servicios/formulario.html',
        {'form': form, 'titulo': 'Nuevo servicio'},
    )


def editar_servicio(request, pk):
    """
    GET: muestra el formulario con los datos actuales del servicio.
    POST: valida y actualiza el servicio existente.
    """
    servicio = get_object_or_404(Servicio, pk=pk)

    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Servicio actualizado correctamente.')
            return redirect('listar_servicios')
    else:
        form = ServicioForm(instance=servicio)

    return render(
        request,
        'servicios/formulario.html',
        {'form': form, 'titulo': f'Editar: {servicio.nombre}'},
    )


def eliminar_servicio(request, pk):
    """
    Solo procesa la eliminación por POST (nunca por un enlace GET),
    con confirmación emergente hecha en la plantilla vía JavaScript.
    """
    servicio = get_object_or_404(Servicio, pk=pk)

    if request.method == 'POST':
        nombre = servicio.nombre
        servicio.delete()
        messages.success(request, f'Servicio "{nombre}" eliminado.')

    return redirect('listar_servicios')
