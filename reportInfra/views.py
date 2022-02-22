from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from .models import *

# Create your views here.

def login(request):

    txtError = ""

    form = AuthenticationForm()    
    if request.method == "POST":               
        form = AuthenticationForm(data=request.POST)         
        if form.is_valid():           
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
                do_login(request, user)
                return redirect('/main')
        else:
            txtError = "Usuario o contraseña incorrectos"            

            
    context = {
        "msg" : txtError,
    }
    return render(request, 'login.html', context)

def logout(request):
    do_logout(request)
    return redirect("/")

@login_required(login_url='/')
def main(request):

    return render(request, 'index.html')

@login_required(login_url='/')
def sr(request):

    form = addData(request.POST or None)

    if request.method == "POST":
       if form.is_valid():            
           print("Si entra")
           frm = form.save(commit=False)           
           frm.save()
           #url = reverse('main')
           #return HttpResponseRedirect(url)
           return redirect('/main')
       else:            
           print("No se grabo nada :(")
    
    context = {
        "titulo" : "SERVICE REQUESTS GENERALES",
        "form": form,
    }

    return render(request, 'sr.html', context)

@login_required(login_url='/')
def reportes(request):

    idTipo = ""
    idT = ""

    if request.GET.get("idTipo", "") == "0":
        idT = ""
    elif request.GET.get("idTipo", "") == "1":
        idT = "DE SOFTWARE"
    elif request.GET.get("idTipo", "") == "2":
        idT = "DE HARDWARE"
    elif request.GET.get("idTipo", "") == "3":
        idT = "DE VMWARE"

    titulo = "FALLAS " + idT + " POR COMPONENTE"
    print(idT)

    idFalla = request.GET.get("idRep", "")
    queryset = ""

    if request.GET.get("idRep", "") == "0":
        queryset = reporteFallas.objects.raw("select * from reportinfra_reportefallas")
    else:
        queryset = reporteFallas.objects.raw("select * from reportinfra_reportefallas where TipoFalla_id = " + idFalla)
    print(queryset)
    context = {
        "qry" : queryset,
        "title" : titulo,

    }

    return render(request, 'reportes.html', context)

@login_required(login_url='/')
def kpis(request):

    return render(request, 'kpis.html')