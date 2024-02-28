from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import Fazenda


def indexFazenda(request):
    fazendas = Fazenda.objects \
        .filter(ativo=True) \
        .order_by('-id')

    paginator = Paginator(fazendas, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Lista de Fazendas - '
    }

    return render(
        request,
        'fazenda/index.html',
        context
    )


def searchFazenda(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('produtorRural:indexFazenda')

    fazenda = Fazenda.objects \
        .filter(ativo=True)\
        .filter(
            Q(nomeFazenda__icontains=search_value) |
            Q(cidade__icontains=search_value) |
            Q(estado__icontains=search_value) |
            Q(areaTotal__icontains=search_value) |
            Q(areaAgricultavel__icontains=search_value) |
            Q(areaVegetacao__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(fazenda, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Busca Fazenda - ',
        'search_value': search_value,
    }

    return render(
        request,
        'fazenda/index.html',
        context
    )


def fazenda(request, fazenda_id):
    single_fazenda = get_object_or_404(
        Fazenda, pk=fazenda_id, ativo=True
    )
    site_title = f'Fazenda - {single_fazenda.nomeFazenda}'

    context = {
        'fazenda': single_fazenda,
        'site_title': site_title
    }

    return render(
        request,
        'fazenda/fazenda.html',
        context
    )

def dashboard(request):
    dashboard = Fazenda.objects \
        .filter(ativo=True) \
        .order_by('-id')

    paginator = Paginator(dashboard, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Dashboard - '
    }

    return render(
        request,
        'dashboard/dashboard.html',
        context
    )