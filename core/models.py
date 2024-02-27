from django.db import models

class Base(models.Model):
    criado = models.DateField('Criação',auto_now_add=True)
    modificado = models.DateField('Atualização',auto_now=True)
    ativo = models.BooleanField('Ativo?',default=True)

    class Meta:
        abstract = True

class ProdutorRural(Base):
    nomeProdutorRural = models.CharField('Nome do Produtor Rural', max_length=100)
    cpfcnpj = models.CharField('CPF/CNPJ', max_length=14)

    class Meta:
        verbose_name = 'ProdutorRural'
        verbose_name_plural = 'ProdudoresRurais'

    def __str__(self):
        return self.nomeProdutorRural

class TipoCultura(Base):
    tipoCultura = models.CharField('Tipo de Cultura', max_length=50)

    class Meta:
        verbose_name = 'TipoCultura'
        verbose_name_plural = 'TiposCultura'

    def __str__(self):
        return self.tipoCultura

class Fazenda(Base):
    ESTADOS_CHOICES = (
        ('ac', 'AC'),
        ('am', 'AM'),
        ('ro', 'RO'),
        ('rr', 'PA'),
        ('ap', 'AP'),
        ('to', 'TO'),
        ('ma', 'MA'),
        ('pi', 'PI'),
        ('ce', 'CE'),
        ('rn', 'RN'),
        ('pb', 'PB'),
        ('pe', 'PE'),
        ('al', 'AL'),
        ('se', 'SE'),
        ('ba', 'BA'),
        ('mg', 'MG'),
        ('es', 'ES'),
        ('rj', 'RJ'),
        ('sp', 'SP'),
        ('pr', 'PR'),
        ('sc', 'SC'),
        ('rs', 'RS'),
        ('ms', 'MS'),
        ('mt', 'MT'),
        ('go', 'GO'),
        ('df', 'DF'),
    )

    produtorRural = models.ForeignKey('core.ProdutorRural', verbose_name='ProdutorRural', on_delete=models.CASCADE)
    nomeFazenda = models.CharField('Nome da Fazenda', max_length=100)
    cidade = models.CharField('Cidade', max_length=100)
    estado = models.CharField('Estado', max_length=2, choices=ESTADOS_CHOICES)
    areaTotal = models.FloatField(null=True, blank=True, default=None)
    areaAgricultavel = models.FloatField(null=True, blank=True, default=None)
    areaVegetacao = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        verbose_name = 'Fazenda'
        verbose_name_plural = 'Fazendas'

    def __str__(self):
        return self.nomeFazenda

class FazendaCulturaPlantada(Base):
    fazenda = models.ForeignKey('core.Fazenda', verbose_name='Fazenda', on_delete=models.CASCADE)
    tipoCultura = models.ForeignKey('core.TipoCultura', verbose_name='TipoCultura', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'FazendaCulturaPlantada'
        verbose_name_plural = 'FazendasCulturasPlantadas'

    def __int__(self):
        return self.fazenda