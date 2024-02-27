from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import ProdutorRural, TipoCultura, Fazenda, FazendaCulturaPlantada

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['produtorural'] = ProdutorRural.objects.all()
        context['tipocultura'] = TipoCultura.objects.all()
        context['fazenda'] = Fazenda.objects.all()
        context['fazendaculturaplantada'] = FazendaCulturaPlantada.objects.all()
        return context