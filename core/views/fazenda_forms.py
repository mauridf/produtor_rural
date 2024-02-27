from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.models import Fazenda
from core.forms import FazendaForm

@login_required(login_url='produtorRural:login')
def createFazenda(request):
    form_action = reverse('produtorRural:createFazenda')

    if request.method == 'POST':
        form = FazendaForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            fazenda = form.save(commit=False)
            fazenda.save()
            return redirect('produtorRural:updateFazenda', fazenda_id=fazenda.pk)

        return render(
            request,
            'fazenda/create.html',
            context
        )

    context = {
        'form': FazendaForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'fazenda/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def updateFazenda(request, fazenda_id):
    fazenda = get_object_or_404(
        Fazenda, pk=fazenda_id, ativo=True
    )
    form_action = reverse('produtorRural:updateFazenda', args=(fazenda_id,))

    if request.method == 'POST':
        form = FazendaForm(request.POST, request.FILES, instance=fazenda)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            fazenda = form.save()
            return redirect('produtorRural:updateFazenda', fazenda_id=fazenda.pk)

        return render(
            request,
            'fazenda/create.html',
            context
        )

    context = {
        'form': FazendaForm(instance=fazenda),
        'form_action': form_action,
    }

    return render(
        request,
        'fazenda/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def deleteFazenda(request, fazenda_id):
    fazenda = get_object_or_404(
        Fazenda, pk=fazenda_id, ativo=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        fazenda.delete()
        return redirect('produtorRural:indexFazenda')

    return render(
        request,
        'fazenda/fazenda.html',
        {
            'fazenda': fazenda,
            'confirmation': confirmation,
        }
    )