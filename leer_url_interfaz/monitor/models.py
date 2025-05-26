from django.db import models

class UrlMonitor(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=32, blank=True, null=True)
    has_changed = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    last_checked = models.DateTimeField(blank=True, null=True)

    # NUEVOS CAMPOS para detectar errores
    status_code = models.IntegerField(blank=True, null=True)  
    is_failed = models.BooleanField(default=False)            

    def __str__(self):
        return self.url


class BoletinUrl(models.Model):
    url = models.URLField()
    hash = models.CharField(max_length=32, blank=True, null=True)
    has_changed = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)
    last_checked = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.url

# nuevo codigo Alejandro 19/5/2025 se implementa codigo para filtrado
from django.db import models

class Filtro(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    palabras = models.TextField()  # palabras separadas por coma
    archivo = models.FileField(upload_to='filtros/', null=True, blank=True) 
# nuevo codigo Alejandro 21/5/2025 se implementa codigo para filtrado
    

# nuevo codigo Alejandro 21/5/2025 se implementa codigo para filtrado
    def __str__(self):
        return self.nombre
    
# nuevo codigo Alejandro 19/5/2025 se implementa codigo para filtrado
# modificado por Samuel 21/05/2025
class FiltroGenerico(models.Model):
    nombre = models.CharField(max_length=100)
    palabras = models.TextField()  # <-- Este campo debe existir

    def __str__(self):
        return self.nombre