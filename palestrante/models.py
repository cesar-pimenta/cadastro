from django.db import models
from django.utils.formats import number_format

# Create your models here.

class Palestrante(models.Model):
    tema = models.CharField(max_length=100, null=True, blank=True,)
    palestrante = models.CharField(max_length=100, null=True, blank=True,)
    cargo = models.CharField(max_length=100, null=True, blank=True,)
    resumo = models.TextField(null=True, blank=True,)
    email = models.CharField(max_length=100, null=True, blank=True,)
    telefone = models.CharField(max_length=100, null=True, blank=True,)

    class Meta:
        ordering = ['palestrante']
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.palestrante

    full_name = property(__str__)