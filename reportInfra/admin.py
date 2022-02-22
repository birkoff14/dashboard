from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    pass

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    pass

@admin.register(CambioHW)
class CambioHWAdmin(admin.ModelAdmin):
    pass

@admin.register(TipoFalla)
class TipoFallaAdmin(admin.ModelAdmin):
    pass

@admin.register(Componente)
class ComponenteAdmin(admin.ModelAdmin):
    pass

@admin.register(reporteFallas)
class reporteFallasAdmin(ImportExportModelAdmin):
    list_display = ("SR", "descripcion", "Usuario", "Fecha", "Vendor", "Componente", "Ambiente", "CambioHW", "timestamp")