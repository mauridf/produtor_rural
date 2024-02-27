from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.models import TipoCultura
from core.forms import TipoCulturaForm

@login_required(login_url='produtorRural:login')
def createTipoCultura(request):
    form_action = reverse('produtorRural:createTipoCultura')

    if request.method == 'POST':
        form = TipoCulturaForm(request.POST)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            tipoCultura = form.save(commit=False)
            tipoCultura.save()
            return redirect('produtorRural:updateTipoCultura', tipoCultura_id=tipoCultura.pk)

        return render(
            request,
            'tipo_cultura/create.html',
            context
        )

    context = {
        'form': TipoCulturaForm(),
        'form_action': form_action,
    }

    return render(
        request,
        'tipo_cultura/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def updateTipoCultura(request, tipoCultura_id):
    tipoCultura = get_object_or_404(
        TipoCultura, pk=tipoCultura_id, ativo=True
    )
    form_action = reverse('produtorRural:updateTipoCultura', args=(tipoCultura_id,))

    if request.method == 'POST':
        form = TipoCulturaForm(request.POST, request.FILES, instance=tipoCultura)

        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            tipoCultura = form.save()
            return redirect('produtorRural:updateTipoCultura', tipoCultura_id=tipoCultura.pk)

        return render(
            request,
            'tipo_cultura/create.html',
            context
        )

    context = {
        'form': TipoCulturaForm(instance=tipoCultura),
        'form_action': form_action,
    }

    return render(
        request,
        'tipo_cultura/create.html',
        context
    )


@login_required(login_url='produtorRural:login')
def deleteTipoCultura(request, tipoCultura_id):
    tipoCultura = get_object_or_404(
        TipoCultura, pk=tipoCultura_id, ativo=True
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        tipoCultura.delete()
        return redirect('produtorRural:indexTipoCultura')

    return render(
        request,
        'tipo_cultura/tipo_cultura.html',
        {
            'tipoCultura': tipoCultura,
            'confirmation': confirmation,
        }
    )