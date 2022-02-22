from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse

from .models import Componente

def get_componentes(request):
    id_Vendor = request.GET.get('id_Vendor')
    componentes = Componente.objects.none()
    options = '<option value="" selected="selected">---------</option>'
    if id_Vendor:
        componentes = Componente.objects.filter(idVendor=id_Vendor)   
        print(componentes.query)
    for componente in componentes:
        options += '<option value="%s">%s</option>' % (
            componente.idComponente,
            componente.Componente
        )
        print(options)
    else:
        print("no entro")
    response = {}
    response['componentes'] = options
    #print(response)
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