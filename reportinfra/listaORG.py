from django.http import JsonResponse
from .models import kpisORG


def obtener_datos(request):
    datos = list(kpisORG.objects.values("id", "ORGvDC"))
    return JsonResponse({"data": datos})