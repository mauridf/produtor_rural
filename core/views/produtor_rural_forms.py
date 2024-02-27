from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.models import ProdutorRural
from core.forms import ProdutorRuralForm

@login_required(login_url='produtorRural:login')
def create(request):
    form_action = reverse('produtorRural:create')

    if request.method == 'POST':
        form = ProdutorRuralForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            produtorRural = form.save(commit=False)
            produtorRural.save()
            return redirect('produtorRural:update', produtor_id=produtorRural.pk)

        return render(
            request,
            'produtor_rural/create.html',
            context
        )

    context = {
        'form': ProdutorRuralForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'produtor_rural/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def update(request, produtor_id):
    produtor = get_object_or_404(
        ProdutorRural, pk=produtor_id, ativo=True
    )
    form_action = reverse('produtorRural:update', args=(produtor_id,))

    if request.method == 'POST':
        form = ProdutorRuralForm(request.POST, request.FILES, instance=produtor)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            produtor = form.save()
            return redirect('produtorRural:update', produtor_id=produtor.pk)

        return render(
            request,
            'produtor_rural/create.html',
            context
        )

    context = {
        'form': ProdutorRuralForm(instance=produtor),
        'form_action': form_action,
    }

    return render(
        request,
        'produtor_rural/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def delete(request, produtor_id):
    produtor = get_object_or_404(
        ProdutorRural, pk=produtor_id, ativo=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        produtor.delete()
        return redirect('produtorRural:index')

    return render(
        request,
        'produtor_rural/produtor_rural.html',
        {
            'produtor': produtor,
            'confirmation': confirmation,
        }
    )