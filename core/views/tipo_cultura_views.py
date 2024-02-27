from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import TipoCultura


def indexTipoCultura(request):
    tipoCultura = TipoCultura.objects \
        .filter(ativo=True)\
        .order_by('-id')

    paginator = Paginator(tipoCultura, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Lista Tipo de Cultura - '
    }

    return render(
        request,
        'tipo_cultura/index.html',
        context
    )


def searchTipoCultura(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('produtorRural:indexTipoCultura')

    tipoCultura = TipoCultura.objects \
        .filter(ativo=True)\
        .filter(
            Q(tipoCultura__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(tipoCultura, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Busca Tipo de Cultura - ',
        'search_value': search_value,
    }

    return render(
        request,
        'tipo_cultura/index.html',
        context
    )


def tipoCultura(request, tipoCultura_id):
    single_tipoCultura = get_object_or_404(
        TipoCultura, pk=tipoCultura_id, ativo=True
    )
    site_title = f'Tipo Cultura - {single_tipoCultura.tipoCultura}'

    context = {
        'tipoCultura': single_tipoCultura,
        'site_title': site_title
    }

    return render(
        request,
        'tipo_cultura/tipo_cultura.html',
        context
    )