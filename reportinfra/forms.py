from django import forms
from django.contrib.auth.models import User
from .models import reporteFallas, Vendor, CambioHW, Ambiente, Componente, cierreFalla
import datetime
from django.forms import ModelChoiceField

class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.get_full_name()

class addData(forms.ModelForm):
    class Meta:
        model = reporteFallas
        fields = ["SR", "Fecha", "Usuario", "Vendor", "Categoria", "Componente", "Ambiente", "CambioHW", "RMA", "RFC", "IM", "descripcion"]

        SR = forms.CharField()        
        #Fecha = forms.DateTimeField(initial=datetime.date.today().strftime("%Y-%m-%d"), required=False, label="Fecha orale")
        #Fecha = forms.CharField()
        Categoria = forms.CharField()
        Usuario = UserModelChoiceField(label="Usuario", queryset=User.objects.filter(is_active=True).order_by('username'))
        Vendor = ModelChoiceField(queryset=Vendor.objects.all().order_by('NombreVendor'))
        Ambiente = ModelChoiceField(queryset=Ambiente.objects.all().order_by('NombreAmbiente'), widget=forms.Select())
        CambioHW = ModelChoiceField(queryset=CambioHW.objects.all().order_by('NombreHW'))
        Componente = ModelChoiceField(queryset=Componente.objects.all())
        descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":30000, "cols":50}))
        

class comments(forms.ModelForm):
    class Meta:
        model = cierreFalla
        fields = ["idFalla", "ComentarioCierre"]

        Comentarios = forms.CharField()
        idFalla = forms.CharField()