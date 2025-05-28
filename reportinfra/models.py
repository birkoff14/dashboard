from django.db import models
from django.conf import settings
from django.utils import timezone
import uuid

# Create your models here.

class CustomUser(models.Model):
    TipoUser = models.CharField(max_length=100, blank=False)
    Perfil = models.CharField(max_length=100, blank=False)
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
    FechaFix = models.DateTimeField(default=timezone.now, blank=True)
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
    FechaInicio = models.DateTimeField(blank=True, verbose_name="Fecha Inicio")
    FechaFin = models.CharField(max_length=150, blank=True, verbose_name="Fecha Fin")
    HorasInvertidas = models.CharField(max_length=50, blank=True, verbose_name="Horas invertidas")
    MinutosInvertidos = models.CharField(max_length=50, blank=True, verbose_name="Minutos invertidos")
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
    Actividades = models.CharField(max_length=100, blank=True, verbose_name="Actividades") #debe ser un catálogo
    

class ingActividad(models.Model):
    NombreIngeniero = models.CharField(max_length=1000, blank=True, verbose_name="Ing. Asignado")
    Proyecto = models.CharField(max_length=150, blank=True, verbose_name="Proyecto")
    Avance = models.CharField(max_length=150, blank=True, verbose_name="Avance")
    Status = models.CharField(max_length=150, blank=True, verbose_name="Status")
    FechaAsignacion = models.DateTimeField(blank=True, verbose_name="Fecha asignación")
    FechaFinal = models.DateTimeField(blank=True, verbose_name="Fecha final")
    LiderTecnico = models.CharField(max_length=150, blank=True, verbose_name="Ing. Asignado")

class Cloud(models.Model):
    idCloud = models.AutoField(primary_key=True)
    Cloud = models.CharField(max_length=200, blank=True, verbose_name="Cloud")
    metadata = models.CharField(max_length=20, blank=True, verbose_name="tipoMetadata")
    def __str__(self):
        return self.Cloud

class Folder(models.Model):
    idCloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, null=True, verbose_name="Cloud")
    Folder = models.CharField(max_length=200, blank=True, verbose_name="Folder")
    def __str__(self):
        return self.Folder
    

class Keepass(models.Model):
    Cloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, null=True, verbose_name="Cloud")
    Titulo = models.CharField(max_length=150, blank=True, verbose_name="Titulo")
    Usuario = models.CharField(max_length=150, blank=True, verbose_name="Usuario")
    Password = models.CharField(max_length=150, blank=True, verbose_name="Password")
    URL = models.CharField(max_length=150, blank=True, verbose_name="URL")
    FechaExpiracion = models.DateTimeField(blank=True, verbose_name="Fecha Expiración")
    Nota = models.TextField(null=True, verbose_name="Nota")
    Folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, verbose_name="Folder")
    Fecha = models.DateTimeField(blank=True, verbose_name="Fecha modificación")
    idUsuario = models.CharField(max_length=50, blank=True, verbose_name="ID User")

class kpisORG(models.Model):
    idCloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, null=True, verbose_name="Cloud")
    ORG = models.CharField(max_length=150, blank=True, verbose_name="Organización")
    ORGvDC = models.CharField(max_length=150, blank=True, verbose_name="Nombre OrgvDC")
    NombreORG = models.CharField(max_length=150, blank=True, verbose_name="Nombre Organización")
    vApp = models.CharField(max_length=150, blank=True, verbose_name="Nombre vApp")
    VM = models.CharField(max_length=150, blank=True, verbose_name="Nombre VM")
    OS = models.CharField(max_length=150, blank=True, verbose_name="Sistema Operativo")
    NoUsuarios = models.CharField(max_length=150, blank=True, verbose_name="No Usuarios")
    FechaAlta = models.CharField(max_length=150, blank=True, verbose_name="Fecha Alta")
    timestamp = models.DateTimeField(blank=True, verbose_name="Timestamp")
    Suscripcion = models.CharField(max_length=150, blank=True, verbose_name="Suscripcion")
    UUID = models.UUIDField(default=uuid.uuid4, editable=True)
    UUIDVM = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name="UUIDVM")

class metadataORG(models.Model):
    idORG = models.CharField(max_length=150, blank=True, verbose_name="ID Org")
    ORGname = models.CharField(max_length=150, blank=True, verbose_name="Nombre")
    SAP = models.CharField(max_length=5000, blank=True, verbose_name="SAP")
    TipoContratacion = models.CharField(max_length=5000, blank=True, verbose_name="Tipo Contratacion")
    SA_Panel = models.CharField(max_length=5000, blank=True, verbose_name="SA Panel")
    UUID = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name="UUID")
    
class metadataORGvDC(models.Model):
    idORG = models.CharField(max_length=150, blank=True, verbose_name="ID Org")
    Campo = models.CharField(max_length=20, blank=True, verbose_name="Campo")
    Valor = models.CharField(max_length=250, blank=True, verbose_name="Valor")
    UUID = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name="UUID")
    UUIDVDC = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name="UUIDVCD")
   
class metadataVM(models.Model):
    idORG = models.CharField(max_length=150, blank=True, verbose_name="ID Org")
    VM = models.CharField(max_length=250, blank=True, verbose_name="VM")
    cpu = models.CharField(max_length=150, blank=True, verbose_name="CPU")
    memoria = models.CharField(max_length=150, blank=True, verbose_name="Memoria")
    host = models.CharField(max_length=150, blank=True, verbose_name="ESX")
    computePolicy = models.CharField(max_length=150, blank=True, verbose_name="Compute")
    idVM = models.CharField(max_length=150, blank=True, verbose_name="IDVM")
    hdd = models.CharField(max_length=150, blank=True, verbose_name="HDD")
    UUID = models.UUIDField(default=uuid.uuid4, editable=True)
    UUIDVDC = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name="UUIDVCD")
    UUIDVM = models.UUIDField(default=uuid.uuid4, editable=True, verbose_name="UUIDVM")
        
class esx(models.Model):
    idvCenter = models.CharField(max_length=150, blank=True, verbose_name="vCenter")
    ESX = models.CharField(max_length=150, blank=True, verbose_name="ESX")
    Vendor = models.CharField(max_length=150, blank=True, verbose_name="Vendor")
    Host = models.CharField(max_length=150, blank=True, verbose_name="Host")
    idCloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, null=True, verbose_name="Cloud")
    #UUID = models.UUIDField(default=uuid.uuid4, editable=True)
    
class vmESX(models.Model):
    idvCenter = models.CharField(max_length=150, blank=True, verbose_name="vCenter")
    name = models.CharField(max_length=150, blank=True, verbose_name="Nombre")
    VM = models.CharField(max_length=150, blank=True, verbose_name="VM")
    State = models.CharField(max_length=150, blank=True, verbose_name="Estado")
    idCloud = models.ForeignKey(Cloud, on_delete=models.CASCADE, null=True, verbose_name="Cloud")
    #UUID = models.UUIDField(default=uuid.uuid4, editable=True)