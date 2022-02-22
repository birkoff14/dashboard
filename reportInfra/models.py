from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Vendor(models.Model):
    idVendor = models.AutoField(primary_key=True)
    NombreVendor = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.NombreVendor
    class Meta:
        ordering = ['NombreVendor']

class Ambiente(models.Model):
    idAmbiente = models.AutoField(primary_key=True)
    NombreAmbiente = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.NombreAmbiente
    class Meta:
        ordering = ['NombreAmbiente']

class CambioHW(models.Model):
    idHW = models.AutoField(primary_key=True)
    NombreHW = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.NombreHW
    class Meta:
        ordering = ['idHW']

class TipoFalla(models.Model):
    idTipo = models.AutoField(primary_key=True)
    Falla = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.Falla
    class Meta:
        ordering = ['Falla']

class Componente(models.Model):    
    idComponente = models.AutoField(primary_key=True)
    idVendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, verbose_name="Vendor")
    Componente = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.Componente
    class Meta:
        ordering = ['Componente']

class reporteFallas(models.Model):
    SR = models.CharField(max_length=150, blank=True, verbose_name="Service Request")
    descripcion = models.TextField(null=True, verbose_name="Descripcion")
    Usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    ) 
    Fecha = models.CharField(max_length=50, blank=False)
    Vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, verbose_name="Vendor")
    Ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, null=True, verbose_name="Ambiente")
    CambioHW = models.ForeignKey(CambioHW, on_delete=models.CASCADE, null=True, verbose_name="Cambio de hardware")
    Componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, verbose_name="Componente")
    TipoFalla = models.ForeignKey(TipoFalla, on_delete=models.CASCADE, null=True, verbose_name="Tipo de falla")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")