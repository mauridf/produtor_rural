from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.models import FazendaCulturaPlantada
from core.forms import CulturaPlantadaForm

@login_required(login_url='produtorRural:login')
def createCulturaPlantada(request):
    form_action = reverse('produtorRural:createCulturaPlantada')

    if request.method == 'POST':
        form = CulturaPlantadaForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            culturaPlantada = form.save(commit=False)
            culturaPlantada.save()
            return redirect('produtorRural:updateCulturaPlantada', culturaPlantada_id=culturaPlantada.pk)

        return render(
            request,
            'cultura_plantada/create.html',
            context
        )

    context = {
        'form': CulturaPlantadaForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'cultura_plantada/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def updateCulturaPlantada(request, culturaPlantada_id):
    culturaPlantada = get_object_or_404(
        FazendaCulturaPlantada, pk=culturaPlantada_id, ativo=True
    )
    form_action = reverse('produtorRural:updateCulturaPlantada', args=(culturaPlantada_id,))

    if request.method == 'POST':
        form = CulturaPlantadaForm(request.POST, request.FILES, instance=culturaPlantada)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            culturaPlantada = form.save()
            return redirect('produtorRural:updateCulturaPlantada', culturaPlantada_id=culturaPlantada.pk)

        return render(
            request,
            'cultura_plantada/create.html',
            context
        )

    context = {
        'form': CulturaPlantadaForm(instance=culturaPlantada),
        'form_action': form_action,
    }

    return render(
        request,
        'cultura_plantada/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def deleteCulturaPlantada(request, culturaPlantada_id):
    culturaPlantada = get_object_or_404(
        FazendaCulturaPlantada, pk=culturaPlantada_id, ativo=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        culturaPlantada.delete()
        return redirect('produtorRural:indexCulturaPlantada')

    return render(
        request,
        'cultura_plantada/cultura_plantada.html',
        {
            'culturaPlantada': culturaPlantada,
            'confirmation': confirmation,
        }
    )