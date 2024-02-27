from django.contrib import admin

from .models import ProdutorRural, TipoCultura, Fazenda, FazendaCulturaPlantada

@admin.register(ProdutorRural)
class ProdutorRuralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nomeProdutorRural', 'cpfcnpj', 'ativo','criado', 'modificado')
    ordering = '-id',
    list_filter = 'criado',
    search_fields = 'id', 'nomeProdutorRural', 'cpfcnpj',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'ativo',
    list_display_links = 'id', 'cpfcnpj',

@admin.register(TipoCultura)
class TipoCulturaAdmin(admin.ModelAdmin):
    list_display = ('tipoCultura', 'ativo', 'criado', 'modificado')

@admin.register(Fazenda)
class FazendaAdmin(admin.ModelAdmin):
    list_display = ('produtorRural','nomeFazenda','cidade','estado','ativo', 'criado', 'modificado')

@admin.register(FazendaCulturaPlantada)
class FazendaCulturaPlantadaAdmin(admin.ModelAdmin):
    list_display = ('fazenda','tipoCultura','ativo', 'criado', 'modificado')