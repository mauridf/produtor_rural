from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import FazendaCulturaPlantada


def indexCulturaPlantada(request):
    culturaPlantada = FazendaCulturaPlantada.objects \
        .filter(ativo=True)\
        .order_by('-id')

    paginator = Paginator(culturaPlantada, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Lista de Culturas Plantadas - '
    }

    return render(
        request,
        'cultura_plantada/index.html',
        context
    )


def searchCulturaPlantada(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('produtorRural:indexCulturaPlantada')

    culturaPlantada = FazendaCulturaPlantada.objects \
        .filter(ativo=True)\
        .filter(
            Q(tipoCultura__icontains=search_value) |
            Q(fazenda__icontains=search_value)
        )\
        .order_by('id')

    paginator = Paginator(culturaPlantada, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Busca Cultura Plantada - ',
        'search_value': search_value,
    }

    return render(
        request,
        'cultura_plantada/index.html',
        context
    )


def culturaPlantada(request, culturaPlantada_id):
    single_culturaPlantada = get_object_or_404(
        FazendaCulturaPlantada, pk=culturaPlantada_id, ativo=True
    )
    site_title = f'Cultura Plantada - {single_culturaPlantada.fazenda} - {single_culturaPlantada.tipoCultura}'

    context = {
        'culturaPlantada': single_culturaPlantada,
        'site_title': site_title
    }

    return render(
        request,
        'cultura_plantada/cultura_plantada.html',
        context
    )