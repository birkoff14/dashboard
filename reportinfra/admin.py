from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Vendor)
class VendorAdmin(ImportExportModelAdmin):
    list_display = ("idVendor", "idCategoria", "NombreVendor")

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    pass

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
    list_display = ("SR", "descripcion", "Usuario", "Fecha", "Vendor", "Categoria", "Componente", "Ambiente", "CambioHW", "timestamp")