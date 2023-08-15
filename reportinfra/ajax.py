from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

from .models import Componente, Vendor, Folder

def get_componentes(request):
    id_Vendor = request.GET.get('id_Vendor')
    componentes = Componente.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_Vendor:
        componentes = Componente.objects.filter(idVendor=id_Vendor)   
    for componente in componentes:
        options += '<option value="%s">%s</option>' % (
            componente.idComponente,
            componente.Componente
        )
    
    response = {}
    response['componentes'] = options
    return JsonResponse(response)

def get_vendors(request):
    id_Categoria = request.GET.get('id_Categoria')
    categorias = Vendor.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_Categoria:
        categorias = Vendor.objects.filter(idCategoria=id_Categoria)
    for categoria in categorias:
        options += '<option value="%s">%s</option>' % (
            categoria.idVendor,
            categoria.NombreVendor
        )
    response = {}
    response['categorias'] = options
    return JsonResponse(response)

def get_folder(request):
    id_Cloud = request.GET.get('id_Cloud')
    folders = Folder.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_Cloud:
        folders = Folder.objects.filter(idCloud=id_Cloud)
        print(folders.query)
    for folder in folders:
        options += '<option value="%s">%s</option>' % (
            folder.idCloud,
            folder.Folder,
        )
    response = {}
    response['folders'] = options

    return JsonResponse(response)


#solo en caso de que se necesiten más de dos select anidados
#def get_localidades(request):
#    municipio_id = request.GET.get('municipio_id')
#    localidades = Localidad.objects.none()
#    options = '<option value="" selected="selected">---------</option>'
#    if municipio_id:
#        localidades = Localidad.objects.filter(municipio_id=municipio_id)   
#    for localidad in localidades:
#        options += '<option value="%s">%s</option>' % (
#            localidad.pk,
#            localidad.localidad
#        )
#    response = {}
#    response['localidades'] = options
#    return JsonResponse(response)