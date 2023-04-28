from django import forms
from django.contrib.auth.models import User
from django.forms import ModelChoiceField, DateField
from .models import reporteFallas, Vendor, CambioHW, Ambiente, Componente, cierreFalla, actividades
import datetime


class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()

class addData(forms.ModelForm):
    class Meta:
        model = reporteFallas

        fields = ['SR', 'Fecha', 'Usuario', 'Vendor', 'Categoria', 'Componente', 'Ambiente', 'CambioHW', 'RMA', 'RFC', 'IM', 'descripcion',  'FechaHoraSolicitud', 'FechaPrimerContacto', 'FechaCierre', 'EstatusSR', 'Severidad', 'Resolucion']

class comments(forms.ModelForm):
    class Meta:
        model = cierreFalla
        fields = ["idFalla", "ComentarioCierre"]

        Comentarios = forms.CharField()
        idFalla = forms.HiddenInput()


class dailyLog(forms.ModelForm):
    class Meta:
        model = actividades
        fields = ["TipoActividad", "FechaInicio", "FechaFin", "HorasInvertidas"]

        TipoActividad = ModelChoiceField(queryset=actividades.objects.values_list('id','TipoActividad'))
        
        #raw("select case when (LENGTH(SR) = 0 and length(RFC) = 0)  then IM when (LENGTH(IM) = 0 and length(RFC) = 0)  then SR when (LENGTH(SR) = 0 and length(IM) = 0)  then RFC else SR end SR"))

class activities(forms.ModelForm):
    class Meta:
        model = actividades
        fields = "__all__"

        AmbienteTest = ModelChoiceField(queryset=Ambiente.objects.all().order_by('NombreAmbiente'), widget=forms.Select())