from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario = models.CharField(max_length=50, blank=False, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)

    class Meta:
        verbose_name = "Usuario"
