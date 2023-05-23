from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class CustomUser(models.Model):
    TipoUser = models.CharField(max_length=100, blank=False)
    Usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


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
    Area = models.CharField(max_length=100, blank=False)
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
    RMA = models.CharField(max_length=150, blank=True)
    RFC = models.CharField(max_length=50, blank=True)
    IM = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")
    FechaHoraSolicitud = models.CharField(max_length=150, blank=True, verbose_name="Fecha Solicitud")
    FechaPrimerContacto = models.CharField(max_length=150, blank=True, verbose_name="Fecha Primer Contacto")
    FechaCierre = models.CharField(max_length=150, blank=True, verbose_name="Fecha Cierre")
    EstatusSR = models.CharField(max_length=150, blank=True, verbose_name="Estatus")
    Severidad = models.CharField(max_length=150, blank=True, verbose_name="Severidad")
    Resolucion = models.CharField(max_length=150, blank=True, verbose_name="Resolución")

class cierreFalla(models.Model):
    idFalla = models.CharField(max_length=150, blank=True, verbose_name="Service Request")
    ComentarioCierre = models.TextField(null=True, verbose_name="Comentario")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")

class actividades(models.Model):
    TipoActividad = models.CharField(max_length=150, blank=True, verbose_name="Actividad")
    FechaInicio = models.DateTimeField(default=timezone.now, blank=True, verbose_name="Fecha Inicio")
    FechaFin = models.CharField(max_length=150, blank=True, verbose_name="Fecha Fin")
    HorasInvertidas = models.CharField(max_length=50, blank=True, verbose_name="Horas invertidas")
    IM = models.CharField(max_length=150, blank=True, verbose_name="IM")
    RFC = models.CharField(max_length=150, blank=True, verbose_name="RFC")
    SR = models.CharField(max_length=150, blank=True, verbose_name="SR")
    Usuario = models.CharField(max_length=150, blank=True, verbose_name="Usuario")
    Evento = models.CharField(max_length=150, blank=True, verbose_name="Evento")
    Descripcion = models.CharField(max_length=500, blank=True, verbose_name="Descripción")
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Fecha")
    Ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE, null=True, verbose_name="Ambiente")
    Status = models.CharField(max_length=150, blank=True, verbose_name="Status")
    Avance = models.CharField(max_length=150, blank=True, verbose_name="Avance")
    Solicitante = models.CharField(max_length=100, blank=True, verbose_name="Solicitante")
    NombreTurnos = models.CharField(max_length=100, blank=True, verbose_name="NombreTurnos")
    HO = models.CharField(max_length=100, blank=True, verbose_name="Home Office")
    Tipo = models.CharField(max_length=100, blank=True, verbose_name="Tipo mejora") #debe ser un catálogo

class ingActividad(models.Model):
    NombreIngeniero = models.CharField(max_length=150, blank=True, verbose_name="Ing. Asignado")
    Proyecto = models.CharField(max_length=150, blank=True, verbose_name="Proyecto")
    Avance = models.CharField(max_length=150, blank=True, verbose_name="Avance")
    Status = models.CharField(max_length=150, blank=True, verbose_name="Status")
    FechaAsignacion = models.DateTimeField(blank=True, verbose_name="Fecha asignación")
    FechaFinal = models.DateTimeField(blank=True, verbose_name="Fecha final")