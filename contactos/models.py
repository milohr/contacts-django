from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    telefono = models.CharField(primary_key=True, max_length=15,)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.nombre
