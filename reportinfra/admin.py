from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display = ("idVendor", "idCategoria", "NombreVendor")

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ("NombreAmbiente", "Area")

@admin.register(CambioHW)
class CambioHWAdmin(admin.ModelAdmin):
    pass

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass

@admin.register(Componente)
class ComponenteAdmin(ImportExportModelAdmin):
    list_display = ("idVendor", "Componente")
    

@admin.register(reporteFallas)
class reporteFallasAdmin(ImportExportModelAdmin):
    list_display = ("id", "SR", "descripcion", "Usuario", "Fecha", "Vendor", "Categoria", "Componente", "Ambiente", "CambioHW", "timestamp")
    list_filter = ["Usuario", "Ambiente"]

@admin.register(actividades)
class actividadesAdmin(ImportExportModelAdmin):
    list_display = ("FechaInicio", "HorasInvertidas", "Usuario", "Evento", "Descripcion", "Ambiente")

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("Usuario", "TipoUser")

@admin.register(ingActividad)
class ingActividadAdmin(admin.ModelAdmin):
    list_display = ('NombreIngeniero', 'Proyecto', 'Avance', 'Status', 'FechaAsignacion', 'FechaFinal', 'LiderTecnico')
    list_filter = ["NombreIngeniero", "Status"]


@admin.register(Keepass)
class ComponenteAdmin(ImportExportModelAdmin):
    list_display = ('Cloud', 'Titulo', 'Usuario', 'Password', 'URL', 'FechaExpiracion', 'Folder')

@admin.register(Folder)
class FolderAdmin(ImportExportModelAdmin):
    list_display = ('idCloud', 'Folder')

@admin.register(Cloud)
class CloudAdmin(admin.ModelAdmin):
    pass