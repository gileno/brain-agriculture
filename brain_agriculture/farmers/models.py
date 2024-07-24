from django.db import models

from localflavor.br.validators import BRCNPJValidator, BRCPFValidator

from brain_agriculture.core.models import BaseModel

from brain_agriculture.farmers import constants


class City(BaseModel):

    name = models.CharField('Nome', max_length=50)
    state = models.CharField('Estado', max_length=2, choices=constants.StateChoices.choices)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['state', 'name']


class Culture(BaseModel):

    name = models.CharField('Nome', max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Cultura Plantada'
        verbose_name_plural = 'Culturas Plantadas'
        ordering = ['name']


class Farmer(BaseModel):

    name = models.CharField('Nome do produtor', max_length=50)
    farm_name = models.CharField('Nome da fazenda', max_length=50)
    person_type = models.CharField('Tipo da Pessoa', choices=constants.PersonTypeChoices.choices, max_length=2)
    document = models.CharField('Documento', max_length=18)
    city = models.ForeignKey(City, models.PROTECT, verbose_name='Cidade', related_name='farmers')
    total_area = models.DecimalField('Área total (ha)', decimal_places=2, max_digits=8)
    arable_area = models.DecimalField('Área agricultável (ha)', decimal_places=2, max_digits=8)
    vegetation_area = models.DecimalField('Área de vegetação (ha)', decimal_places=2, max_digits=8)
    cultures = models.ManyToManyField(Culture, verbose_name='Culturas Plantadas')

    def __str__(self) -> str:
        return self.name
    
    def clean(self) -> None:
        validator = None
        if self.person_type == constants.PersonTypeChoices.PF:
            validator = BRCPFValidator()
        elif self.person_type == constants.PersonTypeChoices.PJ:
            validator = BRCNPJValidator()
        if validator is not None:
            validator(self.document)
    
    class Meta:
        verbose_name = 'Produtor Rural'
        verbose_name_plural = 'Produtores Rurais'
        ordering = ['name']
        constraints = [
            models.CheckConstraint(
                check=models.Q(total_area__gte=models.F("arable_area") + models.F("vegetation_area")),
                name='check_total_area'
            )
        ]
