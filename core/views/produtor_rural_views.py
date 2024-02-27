from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from core.models import ProdutorRural


def index(request):
    produtores = ProdutorRural.objects \
        .filter(ativo=True)\
        .order_by('-id')

    paginator = Paginator(produtores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Lista - '
    }

    return render(
        request,
        'produtor_rural/index.html',
        context
    )


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('produtorRural:index')

    produtores = ProdutorRural.objects \
        .filter(ativo=True)\
        .filter(
            Q(nomeProdutorRural__icontains=search_value) |
            Q(cpfcnpj__icontains=search_value)
        )\
        .order_by('-id')

    paginator = Paginator(produtores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Busca - ',
        'search_value': search_value,
    }

    return render(
        request,
        'produtor_rural/index.html',
        context
    )


def produtor(request, produtor_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_produtor = get_object_or_404(
        ProdutorRural, pk=produtor_id, ativo=True
    )
    site_title = f'{single_produtor.nomeProdutorRural}'

    context = {
        'produtor': single_produtor,
        'site_title': site_title
    }

    return render(
        request,
        'produtor_rural/produtor_rural.html',
        context
    )
