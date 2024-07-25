from django.db import models


class BaseModel(models.Model):

    is_active = models.BooleanField('Ativo', default=True)
    created_on = models.DateTimeField('Criado em', auto_now_add=True)
    updated_on = models.DateTimeField('Atualizado em', auto_now=True)

    def clean(self):
        pass

    def save(self, *args, **kwargs):
        self.clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
