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
        queryset = reporteFallas.objects.raw("select * from reportinfra_reportefallas where Categoria_id = " + idFalla)
    print(queryset)
    context = {
        "qry" : queryset,
        "title" : titulo,

    }

    return render(request, 'reportes.html', context)

@login_required(login_url='/')
def kpis(request):

    anio = request.GET.get("idY", "")

    print(anio)

    if anio == 0:
       qryplus = "concat(SUBSTRING_INDEX(Fecha, '/', -1)) like '%' "
    else:
        qryplus = "concat(SUBSTRING_INDEX(Fecha, '/', -1)) = '" + anio + "' "

    qry = reporteFallas.objects.raw("select 1 as id, count(*) Total, b.NombreVendor from reportinfra_reportefallas a "
                "inner join reportinfra_vendor b "
                "on a.Vendor_id = b.idVendor where "
                + qryplus + 
                "group by NombreVendor")

    print(qry)


    qryVM = reporteFallas.objects.raw("""
                                      select 1 as id,
monthname(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
SUBSTRING_INDEX(Fecha, '/', 1))) as DateF, count(*) Total
from reportinfra_reportefallas a inner join reportinfra_componente b
on a.Componente_id = b.idComponente inner join reportinfra_vendor c
on a.Vendor_id = c.idVendor
where c.NombreVendor = 'VMware' and """ 
+ qryplus + 
"""
group by month(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
SUBSTRING_INDEX(Fecha, '/', 1)))
order by month(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
SUBSTRING_INDEX(Fecha, '/', 1)))
                                      """)

    qryYear = reporteFallas.objects.raw("select distinct 1 as id, SUBSTRING_INDEX(Fecha, '/', -1) yearF from reportinfra_reportefallas")
    
    context = {
        "qry" : qry,
        "qryVM" : qryVM,
        "qryYear" : qryYear,
    }   

    return render(request, 'kpis.html', context)

def detailSR(request, idSR):

    form = comments(request.POST or None)

    if request.method == "POST":
        if form.is_valid():            
            print("Si entra")
            frm = form.save(commit=False)
            frm.save()
        else:            
            print("No se grabo nada :(")

    context = {
        "Titulo" : "Agregar comentarios de cierre",
        "idSR" : idSR,
        "form": form,

    }
    return render(request, "modal.html", context)

def cierre(request, idSR):

    txtSR = idSR
    qry = reporteFallas.objects.raw("select * from reportinfra_cierrefalla where idFalla = '" + idSR + "'")

    print(idSR)

    context = {
        "Titulo" : "Comentarios para el SR",
        "qry" : qry,
        "txtSR" : txtSR,
    }

    return render(request, "comments.html", context)