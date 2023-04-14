from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from .models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import actividadesSerializer

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
            #print(user)
            if user is not None:
                do_login(request, user)
                return redirect('/main?idU='+username)
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

    usuario = request.GET.get("idU", "")
    print("User: " + usuario)
    _tipoUser = ""

    hoy = datetime.date.today()
    lunes = hoy + datetime.timedelta(0 - hoy.weekday())
    viernes = lunes + datetime.timedelta(days=6)

    qry = actividades.objects.raw("""select 1 as id, Sum(HorasInvertidas) Horas, Usuario
                                    from reportinfra_actividades
                                    where FechaInicio >= '""" + str(lunes) +
                                    """' and (FechaFin <= '""" + str(viernes) + """' and FechaFin <> '')
                                    and Usuario = '""" + usuario + 
                                    """' group by Usuario
                                    order by Usuario""")

    qryTotal = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas), 0) Horas, Usuario
                from reportinfra_actividades
                where Usuario = '""" + usuario +
                """' group by Usuario
                order by Usuario""")

    qryTotalHO = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas), 0) Horas, Usuario
                from reportinfra_actividades
                where Usuario = '""" + usuario +
                """' and HO = 'Si' group by Usuario
                order by Usuario""")

    qryDia = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas), 0) Horas, Usuario
                from reportinfra_actividades
                where FechaInicio >= '""" + str(hoy) + """'
                and (FechaFin <= '""" + str(hoy) + """' and FechaFin <> '')
                and Usuario = '""" + usuario + 
                """' group by Usuario
                order by Usuario""")


    tipoUser = User.objects.raw("""select 1 as id, TipoUser, username from reportinfra_customuser a
                                inner join auth_user b
                                on a.Usuario_id = b.id 
                                where username = '""" + usuario + """'""")

    for user in tipoUser:
        print(f'{user.username} es de tipo {user.TipoUser}')

        _tipoUser = user.TipoUser


    request.session['tipoUser'] = _tipoUser

    print("Esta es mi sesión de tipo: " + request.session['tipoUser'])

    context = {
        "semana" : qry,
        "Total"  : qryTotal,
        "Diario" : qryDia,
        "TotalHO" : qryTotalHO,
        "_tipoUser" : _tipoUser,
    }

    print(qry)

    return render(request, 'index.html', context)

@login_required(login_url='/')
def sr(request):

    form = addData(request.POST or None)
    username = request.GET.get("idU", "")
    urlR = '/main?idU=' + username

    usuarios = {'27':'abraham.desantiago', '18':'adrian.martinez', '2':'angel.lozano', '14':'cynthia.gutierrez', 
        '7':'diego.montoya', '22' : 'eduardo.gonzalez',
        '6':'erik.arroyo', '10':'esdras.orizaba', '19':'eugenio.garcia', '32' : 'gladis.garcia', 
        '3':'hector.ortiz', 
        '23':'ivan.parra', '24':'javier.alvarez', '8':'jorge.ramirez', '26':'jorge.soto', 
        '4':'luis.ramirez', '11':'manuel.meneses', '21':'miguel.banthi ', '16':'patricio.silva', 
        '17':'ricardo.lopez', '12':'tonatiuh.mata',
    }

    usuariosStorage = {'29' : 'abraham.castro', '28' : 'angel.urzua', '31' : 'oscar.salinas', 
        '30' : 'pedro.mendez', '20' : 'rolando.ortega'

    }

    if request.method == "POST":
       print(urlR)
       if form.is_valid():            
           print("Si entra")
           frm = form.save(commit=False)
           frm.save()
           #url = reverse('main')
           #return HttpResponseRedirect(url)           
           return redirect(urlR)
       else:            
           print("No se grabo nada :(")
           print(form.is_valid())
           print(form.errors)

    tipoUser = User.objects.raw("""select 1 as id, TipoUser, username from reportinfra_customuser a
                            inner join auth_user b
                            on a.Usuario_id = b.id 
                            where username = '""" + username + """'""")

    for user in tipoUser:        
        _tipoUser = user.TipoUser

    print("Tipo: " + _tipoUser)

    if _tipoUser == "VMware":
        env = actividades.objects.raw("""select 1 as id, idAmbiente, NombreAmbiente from reportinfra_ambiente where Area = 'VMware' order by 3 """)
        users = usuarios
    else:
        env = actividades.objects.raw("""select 1 as id, idAmbiente, NombreAmbiente from reportinfra_ambiente where Area = 'Storage' order by 3 """)
        users = usuariosStorage

    #print(env)
    #print(users)
    
    context = {
        "titulo" : "SERVICE REQUESTS GENERALES",
        "form": form,
        "usuarios" : users,
        "ambiente" : env
    }

    return render(request, 'sr.html', context)

@login_required(login_url='/')
def reportes(request):

    idTipo = request.GET.get("idTipo", "")
    idT = ""

    fields = """select id, 
                case 
                    when (LENGTH(SR) = 0 and length(RFC) = 0)  then IM
                    when (LENGTH(IM) = 0 and length(RFC) = 0)  then SR
                    when (LENGTH(SR) = 0 and length(IM) = 0)  then RFC
                    else SR
                end SR,
                descripcion, Fecha, RMA, RFC, IM, Ambiente_id, CambioHW_id, Categoria_id, Componente_id, Usuario_id, Vendor_id 
                from reportinfra_reportefallas """


    
    fechaIni = request.POST.get("fechaInit", "0")
    fechaFin = request.POST.get("fechaFin", "0")

    filtroF = """where date(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
              SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
              SUBSTRING_INDEX(Fecha, '/', 1))) between '""" + fechaIni + """' and '""" + fechaFin + """'"""

    filtroC = """ and date(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
              SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
              SUBSTRING_INDEX(Fecha, '/', 1))) between '""" + fechaIni + """' and '""" + fechaFin + """'"""

    #print(filtroF)

    if idTipo == "0":
        idT = ""
    elif idTipo == "1":
        idT = "DE SOFTWARE"
    elif idTipo == "2":
        idT = "DE HARDWARE"
    elif idTipo == "3":
        idT = "DE VMWARE"

    titulo = "FALLAS " + idT + " POR COMPONENTE"
    
    idFalla = request.GET.get("idRep", "")
    queryset = ""

    if request.GET.get("idRep", "") == "0":
        if fechaIni == "0":
            queryset = reporteFallas.objects.raw(fields)
        else:
            queryset = reporteFallas.objects.raw(fields + filtroF)
    else:
        if fechaIni == "0":
            queryset = reporteFallas.objects.raw(fields + " where Categoria_id = " + idFalla)
        else:
            queryset = reporteFallas.objects.raw(fields + " where Categoria_id = " + idFalla + filtroC)

    context = {
        "qry" : queryset,
        "title" : titulo,
        "idRep" : idFalla,
        "idTipo" : idTipo,

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
                                    from reportinfra_reportefallas a left join reportinfra_componente b
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

    print(qryVM)

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

def recover(request):

    context = {
        "Titulo" : "Reportes Fallas Infra",
    }

    return render(request, "recover.html", context)

@login_required(login_url='/')
def activity(request):

    if request.method == "POST":        
        qryInsert = actividades.objects.create(
            TipoActividad=request.POST.get("cmbActividad", ""),
            FechaInicio=request.POST.get("fInicio", ""),
            FechaFin=request.POST.get("fFin", ""),
            HorasInvertidas=request.POST.get("txtHorasInvertidas", ""),
            IM=request.POST.get("IM", ""),
            RFC=request.POST.get("RFC", ""),
            Tipo=request.POST.get("txtTipo", ""),
            Evento=request.POST.get("cmbTipo", ""),
            Usuario=request.POST.get("usuario", ""),
            Descripcion=request.POST.get("Descripcion", ""),
            Ambiente_id=request.POST.get("Ambiente", ""),
            Status=request.POST.get("Status", ""),
            Avance=request.POST.get("Avance", ""),
            Solicitante=request.POST.get("txtSolicitante", ""),
            NombreTurnos=request.POST.get("NombreTurnos", ""),
            HO=request.POST.get("HO", "No"),
        )
        print("Grabo bien los datos del form")
    else:
        print("No se guardo nada")

    #form = dailyLog(request.POST or None)

    username = request.GET.get("idU", "")

    qry = actividades.objects.raw("""select a.id,
            case 
            	when (LENGTH(SR) = 0 and length(RFC) = 0)  then IM
            	when (LENGTH(IM) = 0 and length(RFC) = 0)  then SR
            	when (LENGTH(SR) = 0 and length(IM) = 0)  then RFC
            	else SR
            end SR
            from reportinfra_reportefallas a
            inner join auth_user u on a.Usuario_id = u.id 
            where u.username ='""" + username + """'""")
    
    tipoUser = User.objects.raw("""select 1 as id, TipoUser, username from reportinfra_customuser a
                            inner join auth_user b
                            on a.Usuario_id = b.id 
                            where username = '""" + username + """'""")

    for user in tipoUser:
        #print(f'{user.username} es de tipo {user.TipoUser}')
        _tipoUser = user.TipoUser

    print("Tipo: " + _tipoUser)

    if _tipoUser == "VMware":
        env = actividades.objects.raw("""select 1 as id, idAmbiente, NombreAmbiente from reportinfra_ambiente where Area = 'VMware' order by 3 """)
    else:
        env = actividades.objects.raw("""select 1 as id, idAmbiente, NombreAmbiente from reportinfra_ambiente where Area = 'Storage' order by 3 """)

    print(env)
    
    context = {
        "titulo" : "Registro de actividades",        
        "qry" : qry,
        "env" : env,
    }

    return render(request, 'activities.html', context)

@login_required(login_url='/')
def repactividades(request):

    username = request.GET.get("idU", "")
    fechaIni = request.POST.get("fechaInit", "0")
    fechaFin = request.POST.get("fechaFin", "0")

    if (username == 'adrian.martinez' or username == 'cynthia.gutierrez' or username == 'birkoff'):
        qryWhere = ""
    else:        
        qryWhere = "where Usuario = '" + username + """'"""

    if (fechaIni != "0"):
        qryFecha = " and FechaInicio >= '" + fechaIni + "' and FechaFin <= '" + fechaFin + "'"
    else:
        qryFecha = ""

    #qry = actividades.objects.filter(Usuario="'" + username + "'")
    qry = actividades.objects.raw("""select id,
            case             
	            when (LENGTH(SR) = 0 and length(RFC) = 0)  then IM
	            when (LENGTH(IM) = 0 and length(RFC) = 0)  then SR
	            when (LENGTH(SR) = 0 and length(IM) = 0)  then RFC
            end TipoActividad,  
            FechaInicio, Cast(FechaFin as date) FechaFin, HorasInvertidas, IM, RFC, SR, NombreAmbiente, Status, Avance, Evento, Descripcion, Solicitante, NombreTurnos, Usuario
            from reportinfra_actividades a
            inner join reportinfra_ambiente b
            on b.idAmbiente = a.Ambiente_id """            
            + qryWhere + qryFecha)
    

    print(fechaIni)
    #print(fechaFin)
    print(qry)

    context = {
        "titulo" : "Reporte de actividades",
        "qry" : qry,
        "username" : username,
    }

    return render(request, 'reporteActividades.html', context)

@login_required(login_url='/')
def editSR(request, idSR):

    #band = Band.objects.get(id=id)
    #form = BandForm(instance=band)  # prepopulate the form with an existing band

    qry = reporteFallas.objects.get(SR=idSR)    
    #print(qry)

    form = addData(request.POST or None, instance=qry)

    if request.method == "POST":
       if form.is_valid():            
           print("Si entra")
           frm = form.save(commit=False)           
           frm.save()
           #url = reverse('main')
           #return HttpResponseRedirect(url)
           return redirect('/reportes?idRep=0&idTipo=0')
       else:            
           print("No se grabo nada :(")
    
    context = {
        "Titulo" : "Edición de SR",
        "idSR" : idSR,
        "form": form,
        "qry" : qry,
    }

    return render(request, "editSR.html", context)

@login_required(login_url='/')
def editActivity(request, idAct, idU):

    qry = actividades.objects.get(id=idAct)
    username = idU

    URL = '/repactividades?idU=' + username
    print(URL)

    form = activities(request.POST or None, instance=qry)

    if request.method == "POST":
       if form.is_valid():            
           print("Si entra")
           frm = form.save(commit=False)           
           frm.save()
           #url = reverse('main')
           #return HttpResponseRedirect(url)           
           return redirect(URL)
       else:            
           print("No se grabo nada :(")
    
    context = {
        "Titulo": "Edición de Actividades",
        "form" : form,
        "idAct" : idAct,
        "username" : username,
    }

    return render(request, "editActivity.html", context)

class ActivitiesListApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        act = actividades.objects.filter(Usuario = request.user.id)
        serializer = actividadesSerializer(act, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url='/')
def reporteSemanal(request):
    
    usuario = request.GET.get("idU", "")
    print("User: " + usuario)

    hoy = datetime.date.today()
    lunes = hoy + datetime.timedelta(0 - hoy.weekday())
    viernes = lunes + datetime.timedelta(days=6)


    qry = actividades.objects.raw("""select 1 as id, sum(`HorasInvertidas`) HorasInvertidas, 
                dayname(`FechaInicio`) Dia,
                CONCAT(day(`FechaInicio`), "-", MONTH(`FechaInicio`), "-", YEAR(`FechaInicio`)) as Fecha
                from reportinfra_actividades
                where `Usuario` = '""" + usuario  
                + """' and `FechaInicio` >= '""" + str(lunes) + """' and (FechaFin <= '""" + str(viernes) 
                + """' and FechaFin <> '')"""
                #+ """' and `FechaInicio` >= '2023-03-27' and (FechaFin <= '2023-04-09' and FechaFin <> '') 
                + """ group by day(`FechaInicio`), `FechaInicio`
                order by `FechaInicio`;""")

    print(qry) 

    context = {
        "qry" : qry,
        "userqry" : usuario
    }

    return render(request, "reporteSemanal.html", context)


@login_required(login_url='/')
def detailSemanal(request, fecha, usuario):

    fechaCompuesta = fecha

    my_list = fechaCompuesta.split("-")
    
    qry = actividades.objects.raw("""select * from reportinfra_actividades 
                    where FechaInicio >= '""" + my_list[2] + """-""" + my_list[1] + """-""" + my_list[0] + """ 00:00:00.000000' 
                    and FechaInicio <= '""" + my_list[2] + """-""" + my_list[1] + """-""" + my_list[0] + """ 23:59:00.000000'
                    and Usuario = '""" + usuario + """'""")
    
    print(qry)
       
    context = {
        "qry" : qry
    }
    return render(request, "detalleSemana.html", context)