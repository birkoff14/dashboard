from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    idTipo = models.AutoField(primary_key=True)
    Categoria = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.Categoria
    class Meta:
        ordering = ['Categoria']

class Vendor(models.Model):
    idVendor = models.AutoField(primary_key=True)
    idCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, verbose_name="Vendor")
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
    Categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, verbose_name="Categoria")
    Componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, verbose_name="Componente")
    RMA = models.CharField(max_length=50, blank=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")

class cierreFalla(models.Model):
    idFalla = models.CharField(max_length=150, blank=True, verbose_name="Service Request")
    ComentarioCierre = models.TextField(null=True, verbose_name="Comentario")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")