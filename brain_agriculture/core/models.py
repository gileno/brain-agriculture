from django.db import models


class BaseModel(models.Model):

    is_active = models.BooleanField('Ativo', default=True)
    created_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True
