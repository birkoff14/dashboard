from django.http import JsonResponse
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from .forms import *
from .models import *
from django.core import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .serializers import actividadesSerializer
#import datetime
from datetime import date, timedelta
import calendar
import json

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
    
    primer_dia_mes = hoy.replace(day=1)
    ultimo_dia_mes = hoy.replace(day=calendar.monthrange(hoy.year, hoy.month)[1])
    
    print("Primer día del mes:", primer_dia_mes)
    print("Último día del mes:", ultimo_dia_mes)
    
    
    

    qry = actividades.objects.raw("""select 1 as id, Sum(HorasInvertidas+MinutosInvertidos) Horas, Usuario
                                    from reportinfra_actividades
                                    where FechaInicio >= '""" + str(lunes) +
                                    """' and (FechaFin <= '""" + str(viernes) + """' and FechaFin <> '')
                                    and Usuario = '""" + usuario + 
                                    """' group by Usuario
                                    order by Usuario""")

    qryTotal = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas+MinutosInvertidos), 0) Horas, Usuario
                from reportinfra_actividades
                where Usuario = '""" + usuario +
                """' group by Usuario
                order by Usuario""")

    qryTotalHO = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas+MinutosInvertidos), 0) Horas, Usuario
                from reportinfra_actividades
                where Usuario = '""" + usuario +
                """' and HO = 'Si' group by Usuario
                order by Usuario""")

    qryDia = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas+MinutosInvertidos), 0) Horas, Usuario
                from reportinfra_actividades
                where FechaInicio >= '""" + str(hoy) + """'
                and (FechaFin <= '""" + str(hoy) + """' and FechaFin <> '')
                and Usuario = '""" + usuario + 
                """' group by Usuario
                order by Usuario""")
    
    qryMes = actividades.objects.raw("""select 1 as id, IFNULL(Sum(HorasInvertidas+MinutosInvertidos), 0) Horas, Usuario
                from reportinfra_actividades
                where FechaInicio >= '""" + str(primer_dia_mes) + """'
                and (FechaFin <= '""" + str(ultimo_dia_mes) + """' and FechaFin <> '')
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
        "mes" : qryMes,
        "Total"  : qryTotal,
        "Diario" : qryDia,
        "TotalHO" : qryTotalHO,
        "tipoUser" : _tipoUser,
    }

    print(qry)

    return render(request, 'index.html', context)

@login_required(login_url='/')
def sr(request):

    form = addData(request.POST or None)
    username = request.GET.get("idU", "")
    urlR = '/main?idU=' + username

    usuarios = {'27':'abraham.desantiago', '18':'adrian.martinez', '2':'angel.lozano', 
        '33': 'carlos.rodriguez', '7':'diego.montoya', '22' : 'eduardo.gonzalez',
        '6':'erik.arroyo', '10':'esdras.orizaba', '19':'eugenio.garcia', '32' : 'gladis.garcia', 
        '3':'hector.ortiz', 
        '23':'ivan.parra', '24':'javier.alvarez', '8':'jorge.ramirez', '26':'jorge.soto', 
        '4':'luis.ramirez', '11':'manuel.meneses', '21':'miguel.banthi ', '16':'patricio.silva', 
        '17':'ricardo.lopez', '12':'tonatiuh.mata', '25':'daniel.salcedo', '41' : 'alejandro.godinez', '39' : 'cecilia.lim', 
        '42' : 'diego.abundis','35':'dolores.chavez', '38':'juan.cordova', '37':'miriam.lule', '36':'jose.gomez'
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
                descripcion, FechaFix, RMA, RFC, IM, Ambiente_id, CambioHW_id, Categoria_id, Componente_id, Usuario_id, Vendor_id 
                from reportinfra_reportefallas """


    
    fechaIni = request.POST.get("fechaInit", "0")
    fechaFin = request.POST.get("fechaFin", "0")

    #filtroF = """where date(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
    #          SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
    #          SUBSTRING_INDEX(Fecha, '/', 1))) between '""" + fechaIni + """' and '""" + fechaFin + """'"""

    #filtroC = """ and date(concat(SUBSTRING_INDEX(Fecha, '/', -1), "-",
    #          SUBSTRING_INDEX(SUBSTRING_INDEX(Fecha, '/', 2),'/', -1), "-",
    #          SUBSTRING_INDEX(Fecha, '/', 1))) between '""" + fechaIni + """' and '""" + fechaFin + """'"""

    filtroF = """ where FechaFix between '""" + fechaIni + """ 00:00:00.000000' and '""" + fechaFin + """ 23:59:59.000000'"""

    filtroC = """ and FechaFix between '""" + fechaIni + """ 00:00:00.000000' and '""" + fechaFin + """ 23:59:59.000000'"""

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

    print(queryset)

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

@login_required(login_url='/')
def kpis_supervisor(request):
    
    hoy = datetime.date.today()
    lunes = hoy + datetime.timedelta(0 - hoy.weekday())
    viernes = lunes + datetime.timedelta(days=6)
    
    diaInicio = str(lunes)[-2:]
    diaFin = str(viernes)[-2:]
    mes = str(lunes)[5:7]
 
    qry = actividades.objects.raw("""select 1 as id, sum(HorasInvertidas+MinutosInvertidos) Horas, Usuario 
                                    from reportinfra_actividades
                                    where FechaInicio >= '""" + str(lunes) + """'
                                    and (FechaFin <= '""" + str(viernes) + """' or FechaFin <> '')
                                    group by Usuario""")
    
    print(qry)
    context = {
        "qry" : qry,
        "di" : diaInicio,
        "df" : diaFin,
        "mes" : mes,
    }
    
    return render(request, 'kpis_supervisor.html', context)

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
            SR=request.POST.get("cmbActividad", ""),
            FechaInicio=request.POST.get("fInicio", ""),
            FechaFin=request.POST.get("fFin", ""),
            HorasInvertidas=request.POST.get("cmbHoras", ""),
            MinutosInvertidos=request.POST.get("cmbMinutos", ""),
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
            Actividades=request.POST.get("Actividades", ""),            
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
    
    hoy = datetime.date.today()
    lunes = hoy + datetime.timedelta(0 - hoy.weekday())
    viernes = lunes + datetime.timedelta(days=6)
    
    diaInicio = str(lunes)[-2:]
    diaFin = str(viernes)[-2:]
    mes = str(lunes)[5:7]

    username = request.GET.get("idU", "")
    fechaIni = request.POST.get("fechaInit", str(lunes))
    fechaFin = request.POST.get("fechaFin", str(viernes))
    
    print(fechaFin)

    if (username == 'adrian.martinez' or username == 'pedro.mendez' or username == 'angel.urzua' 
        or username == 'jorge.soto' or username == 'birkoff' or username == 'luis.ramirez'
        or username == 'tonatiuh.mata' or username == 'hector.ortiz' or username == 'erik.arroyo'):
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
            end TipoActividad,  Actividades,
            FechaInicio, Cast(FechaFin as date) FechaFin, HorasInvertidas, IM, RFC, SR, NombreAmbiente, Status, Avance, Evento, Descripcion, Solicitante, NombreTurnos, Usuario
            from reportinfra_actividades a
            inner join reportinfra_ambiente b
            on b.idAmbiente = a.Ambiente_id """            
            + qryWhere + qryFecha)    

    print("Fecha inicio: " + fechaIni)
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

    sr = reporteFallas.objects.values("SR").distinct().order_by("SR")
    
    ambiente = Ambiente.objects.all()
    
    tipo = {'1':'Actualización recurrente', '2':'Implementación', '3':'Toma operativa', 
        '4': 'Trouble shooting falla', '5':'Reuniones de seguimiento', '6' : 'Investigación',
        '7':'Actualización recurrente en curso', '8':'Especial', '9':'Operación',
    }
    
    evento = {'1': 'Evento', '2':'Proyecto'}
    
    estatus = {'1':'En proceso', '2':'Terminado'}
    
    HO = {'1':'Si', '2':'No'}
    
    Solicitante = {'1': 'Adrián Martínez','2': 'Luis Alberto Ramírez','3': 'TEAM OAC','4': 'Turnos', 
                   '5': 'Mesa de ayuda', '6': 'ITOC', '7': 'AMX', '8':'Equipo Triara', '9' : 'Calidad', 
                   '10':'Coordinación de RFC'}
    
    horas = {'1' : '1 hora', '2' : '2 horas', '3' : '3 horas', '4' : '4 horas', '5' : '5 horas', '6' : '6 horas',
             '7' : '7 horas', '8' : '8 horas', '9' : '9 horas', '10' : '10 horas', '11' : '11 horas', '12' : '12 horas',
             '13' : '13 horas', '14' : '14 horas', '15' : '15 horas', '16' : '16 horas', '17' : '17 horas',
             '18' : '18 horas', '19' : '19 horas', '20' : '20 horas', '21' : '21 horas', '22' : '22 horas',
             '23' : '23 horas', '24' : '24 horas'}
    
    minutos = {'0': '00 min', '0.15' : '15 min', '0.30' : '30 min', '0.45' : '45 min'}
    
    act = {'0' : 'Renovación de certificados', '1' : 'Depuración de particiones', '2' : 'Depuración de unidad windows', 
           '3' : 'Actualización de sistema operativo', '4' : 'Actualización de componentes VMware',
           '5' : 'Rotación de password', '6' : 'Recuperación de contraseña', '7' : 'Atención de RFC (Inicio - Seguimiento - Apoyo)', 
           '8' : 'MPLS ABC', '9' : 'External Network', '10' : 'Sesión', '11' : 'Atención de IM escalado', 
           '12' : 'Actividad no categorizada', '13' : 'Healthcheck Guardia', '14' : 'Sanity AMX', '15' : 'Auto-estudio', 
           '16' : 'Guardia Facturación NPE', '17' : 'VLAN VSYS', '18' : 'Alta de usuario', '19' : 'Baja de usuario',
           '20' : 'Generación de reporte', '21' : 'Actvidades de Auditorias', '22' : 'Actividades de Coordinacion de RFC',
           '23' : 'Reemplazo de SFP / NIC', '24' : 'Documentación, análisis y desarrollo de mejora'}
    
    claves = dict(sorted(act.items()))
    print(claves)    
    
    
    qry = actividades.objects.get(id=idAct)
    username = idU
    URL = '/repactividades?idU=' + username

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
        "sr" : sr,
        "ambiente" : ambiente,
        "tipo" : tipo,
        "evento" : evento,
        "estatus" : estatus,
        "HO" : HO,
        "qry" : qry,
        "solicitante" : Solicitante,
        "min" : minutos,
        "hrs" : horas,
        "actividades" : claves,
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


    qry = actividades.objects.raw("""select 1 as id, sum(HorasInvertidas+MinutosInvertidos) HorasInvertidas, 
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

@login_required(login_url='/')
def projects(request):

    qry = ingActividad.objects.raw("""select a.id, a.NombreIngeniero, a.Proyecto, a.Avance, 
        a.Status, a.FechaAsignacion,
        a.FechaFinal, b.first_name, b.last_name, c.username LiderTecnico
        from reportinfra_ingactividad a
        inner join auth_user b
        on a.NombreIngeniero = b.id 
        left join auth_user c
        on a.LiderTecnico = c.id 
        where a.Status != '3' """)
        
    qryTerminado = ingActividad.objects.raw("""select count(*) as Total from reportinfra_ingactividad where Status = 3""")

    context = {
        "qry" : qry,
        "qryTerminado" : qryTerminado,        
    }

    return render(request, "projects.html", context)

@login_required(login_url='/')
def addProject(request, idP):

    usuarios = {'27':'abraham.desantiago', '18':'adrian.martinez', '2':'angel.lozano', 
        '7':'diego.montoya', '22' : 'eduardo.gonzalez',
        '6':'erik.arroyo', '10':'esdras.orizaba', '19':'eugenio.garcia', '32' : 'gladis.garcia', 
        '3':'hector.ortiz', 
        '23':'ivan.parra', '24':'javier.alvarez', '8':'jorge.ramirez', '26':'jorge.soto', 
        '4':'luis.ramirez', '11':'manuel.meneses', '21':'miguel.banthi ', '16':'patricio.silva', 
        '17':'ricardo.lopez', '12':'tonatiuh.mata','25':'daniel.salcedo', '41':'alejandro.godinez', 
        '39':'cecilia.lim', '42':'diego.abundis', '35':'dolores.chavez', '36':'jose.gomez', 
        '37':'miriam.lule', '38':'juan.cordova', 
    }

    lider = {'6' : 'erik.arroyo', '3' : 'hector.ortiz', '11' : 'manuel.meneses', '12' : 'tonatiuh.mata'}
 
    estatus = {'1':'Iniciado', '2' : 'En progreso', '3' : 'Terminado'}

    form = ingProject(request.POST or None)

    if request.method == "POST":
       if form.is_valid():            
           print("Si entra")
           frm = form.save(commit=False)
           frm.save()       
           return redirect("/projects")
       else:            
           print("No se grabo nada :(")
           print(form.is_valid())
           print(form.errors)

    context = {
        "form" : form,
        "user" : usuarios,
        "state" : estatus,
        "boton" : "Agregar proyecto",
        "url" : "addProject",
        "param" : idP,
        "Titulo" : "Agregar proyecto",
        "lider" : lider,
    }

    return render(request, "addProject.html", context)


@login_required(login_url='/')
def editProject(request, idP):

    qry = ingActividad.objects.get(id=idP)    

    usuarios = {'27':'abraham.desantiago', '18':'adrian.martinez', '2':'angel.lozano', 
        '7':'diego.montoya', '22' : 'eduardo.gonzalez',
        '6':'erik.arroyo', '10':'esdras.orizaba', '19':'eugenio.garcia', '32' : 'gladis.garcia', 
        '3':'hector.ortiz', 
        '23':'ivan.parra', '24':'javier.alvarez', '8':'jorge.ramirez', '26':'jorge.soto', 
        '4':'luis.ramirez', '11':'manuel.meneses', '21':'miguel.banthi ', '16':'patricio.silva', 
        '17':'ricardo.lopez', '12':'tonatiuh.mata','25':'daniel.salcedo', '41':'alejandro.godinez', 
        '39':'cecilia.lim', '42':'diego.abundis', '35':'dolores.chavez', '36':'jose.gomez', 
        '37':'miriam.lule', '38':'juan.cordova', 
    }
    
    #usuarios = """SELECT a.id, a.username FROM auth_user a 
    #    inner JOIN reportinfra_customuser b
    #    on a.id = b.Usuario_id
    #    where b.TipoUser = 'VMware'
    #    order by username"""
    
    #data = serializers.serialize('json', ingActividad.objects.raw(usuarios),fields=('id', 'username'))
    
    estatus = {'1':'Iniciado', '2' : 'En progreso', '3' : 'Terminado'}

    lider = {'6' : 'erik.arroyo', '3' : 'hector.ortiz', '11' : 'manuel.meneses', '12' : 'tonatiuh.mata'}

    form = ingProject(request.POST or None, instance=qry)

    if request.method == "POST":
       if form.is_valid():            
           print("Si entra")
           valores = request.POST.getlist('NombreIngeniero')
           for valor in valores:
               print("Valores: " + valor)
               frm = ingActividad(NombreIngeniero=valor)
               #val.save()
               #print(val)
           frm = form.save(commit=False)                      
           frm.save()
           return redirect('/projects')
       else:            
           print("No se grabo nada :(")
    
    context = {
        "Titulo" : "Editar proyecto",
        "form": form,
        "qry" : qry,
        "boton" : "Editar proyecto",
        "user" : usuarios,
        "state" : estatus,
        "url" : "editProject",
        "param" : idP,
        "lider" : lider,
    }

    return render(request, "addProject.html", context)

@login_required(login_url='/')
def keepass(request):

    return render(request, "keepass.html")


@login_required(login_url='/')
def keepass_load(request):

    cloud = request.GET.get('item_id')
    #print(cloud)

    try:
        #qryFolder = Folder.objects.filter(Q(idCloud_id=cloud)).values_list('id', 'Folder', flat=False).distinct()
        qryFolder = Folder.objects.filter(Q(idCloud_id=cloud))
        #print(qryFolder.query)

        items_list = []
        
        for item in qryFolder:       
            #print(item)     
            item_data = {
                'id': item.id,
                'Folder': item.Folder,               
            }

            items_list.append(item_data)

        return JsonResponse(items_list, safe=False)

    except Exception as e:
            return JsonResponse({'error_message': str(e)}, status=500)

    
@login_required(login_url='/')
def get_info(request):

    item_id = request.GET.get('item_id')
    print(item_id)

    try:
        items = Keepass.objects.filter(Q(Folder=item_id))
        
        #print(items.query)        

        items_list = []
        for item in items:            
            item_data = {
                'id': item.id,
                'Titulo': item.Titulo,
                'Usuario' : item.Usuario,
            }
            items_list.append(item_data)
        
        return JsonResponse(items_list, safe=False)
    
    except Exception as e:
        return JsonResponse({'error_message': str(e)}, status=500)
    

def get_info_detail(request):

    item_id = request.GET.get('item_id')
    print(item_id)

    try:
        items = Keepass.objects.filter(Q(id=item_id))
        
        print(items.query)        

        items_list = []
        for item in items:            
            item_data = {
                'id': item.id,
                'Titulo': item.Titulo,
                'Usuario' : item.Usuario,
                'Password' : item.Password,
                'URL' : item.URL,
                'Nota' : item.Nota,
                'Ubicacion' : item.Folder_id,
                'Fecha' : item.Fecha,
                'Editado' : item.idUsuario,
            }

            items_list.append(item_data)
        
        return JsonResponse(items_list, safe=False)
    
    except Exception as e:
        return JsonResponse({'error_message': str(e)}, status=500)
    
def addKeepass(request):
    
    fecha_actual = datetime.date.today()
    #print(fecha_actual)

    cloud = Cloud.objects.all()
    print(cloud.query)
    print(request.POST.get("Cloud", ""))

    form = keepassForm(request.POST or None)

    if request.method == "POST":
         
        if form.is_valid():
           print("Si entra")
           frm = form.save(commit=False)           
           frm.save()
           #url = reverse('main')
           #return HttpResponseRedirect(url)
           return redirect('/keepass')
        else:            
           print("No se grabo nada :(")
           print(form.errors)            

    context = {
        "form": form,
        "cloud" : cloud,
        "timestamp" : fecha_actual,
        "btn" : "Agregar entrada",
        "urlAction" : "/addKeepass/",
    }

    return render(request, "keepassEditAdd.html", context)

def editKeepass(request, idK):

    fecha_actual = datetime.date.today()
    cloud = Cloud.objects.all()
    folder = Folder.objects.all()
    qry = Keepass.objects.get(id=idK)    

    form = keepassForm(request.POST or None, instance=qry)

    if request.method == "POST":
       if form.is_valid():            
           print("Si entra")
           frm = form.save(commit=False)           
           frm.save()
           #url = reverse('main')
           #return HttpResponseRedirect(url)
           return redirect('/keepass')
       else:            
           print("No se grabo nada :(")
           print(form.errors)

    context = {
        "form" : form, 
        "cloud" : cloud,
        "timestamp" : fecha_actual,
        "btn" : "Editar entrada",
        "urlAction" : "/editKeepass/" + idK,
        "qry" : qry,
        "folder" : folder,
    }

    return render(request, 'keepassEditAdd.html', context)


def buscaAllKeepass(request):
    if request.is_ajax():
        filtro = request.GET.get('filtro', None)
        print(filtro)
        if filtro:
            resultados = Keepass.objects.filter(Titulo__icontains=filtro)
            print(resultados.query)
            datos = [{'Titulo': resultado.Titulo, 'Usuario': resultado.Usuario} for resultado in resultados]
            return JsonResponse({'datos': datos})
    return JsonResponse({'error': 'No se pudo realizar la búsqueda'})

def kpiCloud(request):

    idCloud = request.GET.get("idCloud")    
    tagCloud = request.GET.get("id")
    
    
    if tagCloud == 'NET':
        filter = " and ORGvDC like concat(char(37), '_FLEX', char(37))  "
        suscription = " and d.Campo = 'Subscription_ID' "
    else:
        filter = ""
        suscription = ""
        
        
    hoy = datetime.date.today()
    print(hoy)
    
    #totalORG = kpisORG.objects.raw("select 1 as id, count(distinct ORG) ORG from reportinfra_kpisorg where timestamp > '" + str(hoy - timedelta(days=4)) + "'and idCloud_id = " + idCloud + filter)
    totalORG = kpisORG.objects.raw("select 1 as id, count(*) ORG from reportinfra_kpiorgv2 where timestamp > '" + str(hoy) + "' and idCloud_id = " + idCloud)
    #print(totalORG)
    totalVDC = kpisORG.objects.raw("""select 1 as id, count(*) VDC from reportinfra_kpiorgvdcv2 a inner join reportinfra_kpiorgv2 b
                                    on a.UUID_id = b.id where timestamp > '""" + str(hoy) + """'and idCloud_id = """ + idCloud + filter)
    #print(totalVDC)
    totalvPPA = kpisORG.objects.raw("""select 1 as id, count(*) vApps from reportinfra_kpiorgv2 a inner join reportinfra_kpiorgvdcv2 b
                                     on a.id = b.UUID_id inner join reportinfra_kpivappv2 c on b.id = c.idVDC_id 
                                     inner join reportinfra_kpivmv2 d on c.id = d.idvApp_id left join reportinfra_kpimetadatavmv2 e on d.id = e.idvApp_id
                                     where timestamp > '""" + str(hoy) + """'and idCloud_id = """ + idCloud + """ and LENGTH(vApp) < 40 """ + filter)
    
    #print(totalvPPA)
    
    totalVM = kpisORG.objects.raw("""select 1 as id, count(*) VM from reportinfra_kpiorgv2 a inner join reportinfra_kpiorgvdcv2 b
                                  on a.id = b.UUID_id inner join reportinfra_kpivappv2 c on b.id = c.idVDC_id 
                                  inner join reportinfra_kpivmv2 d on c.id = d.idvApp_id left join reportinfra_kpimetadatavmv2 e on d.id = e.idvApp_id 
                                  where timestamp > '""" + str(hoy) + """' and idCloud_id = """ + idCloud + filter)
    #print(totalVM)
    totalWin = kpisORG.objects.raw("""select 1 as id, count(*) Windows from reportinfra_kpiorgv2 a inner join reportinfra_kpiorgvdcv2 b
                                   on a.id = b.UUID_id inner join reportinfra_kpivappv2 c on b.id = c.idVDC_id 
                                   inner join reportinfra_kpivmv2 d on c.id = d.idvApp_id left join reportinfra_kpimetadatavmv2 e on d.id = e.idvApp_id
                                   where a.idCloud_id = """ + idCloud + """ and timestamp > '""" + str(hoy) + """' and OS like concat(char(37), 'Windows', char(37)) """ + filter)
    #print(totalWin)
    totalLinux = kpisORG.objects.raw("""select 1 as id, count(*) Linux from reportinfra_kpiorgv2 a inner join reportinfra_kpiorgvdcv2 b
                                   on a.id = b.UUID_id inner join reportinfra_kpivappv2 c on b.id = c.idVDC_id 
                                   inner join reportinfra_kpivmv2 d on c.id = d.idvApp_id left join reportinfra_kpimetadatavmv2 e on d.id = e.idvApp_id
                                   where a.idCloud_id = """ + idCloud + """ and timestamp > '""" + str(hoy) + """' and OS not like concat(char(37), 'Windows', char(37)) """ + filter)
    
    #print(totalLinux)
    
    reporteORG = kpisORG.objects.raw("""select 1 as id, ORG, ORGvDC, vApp, d.VM, OS, cpu, memoria, hdd 
                                     from reportinfra_kpiorgv2 a inner join reportinfra_kpiorgvdcv2 b on a.id = b.UUID_id
                                     inner join reportinfra_kpivappv2 c on b.id = c.idVDC_id left join reportinfra_kpivmv2 d
                                     on c.id = d.idvApp_id left join reportinfra_kpimetadatavmv2 e on d.id = e.idvApp_id
                                     where idCloud_id = """ + idCloud + """ and timestamp >  '""" + str(hoy) + """' and d.VM is not null """ + filter) 
    
    distros = kpisORG.objects.raw("""select 1 as id,
                                  case
	                                  when OS like concat(char(37), 'Windows', char(37)) then "Windows"
	                                  when OS like concat(char(37), 'CentOS', char(37)) then "CentOS"
	                                  when OS like concat(char(37), 'Debian', char(37)) then "Debian"
	                                  when OS like concat(char(37), 'FreeBSD', char(37)) then "FreeBSD"
	                                  when OS like concat(char(37), 'Oracle', char(37)) then "Oracle"
	                                  when OS like concat(char(37), 'Other', char(37)) then "Linux"
	                                  when OS like concat(char(37), 'Red Hat', char(37)) then "Red Hat"
	                                  when OS like concat(char(37), 'SUSE', char(37)) then "SUSE"
	                                  when OS like concat(char(37), 'UBuntu', char(37)) then "Ubuntu"
	                                  when OS like concat(char(37), 'Photon', char(37)) then "Photon"
	                                  when OS like concat(char(37), 'VMware', char(37)) then "VMware"
	                                  when OS like concat(char(37), 'Amazon', char(37)) then "Amazon"
                                      when OS like concat(char(37), 'Rocky', char(37)) then "Rocky"
                                      when OS like concat(char(37), 'Alma', char(37)) then "AlmaLinux"
                                  end OSClean, Count(*) Total from reportinfra_kpiorgv2 a inner join reportinfra_kpiorgvdcv2 b on a.id = b.UUID_id
                                  inner join reportinfra_kpivappv2 c on b.id = c.idVDC_id inner join reportinfra_kpivmv2 d
                                  on c.id = d.idvApp_id left join reportinfra_kpimetadatavmv2 e on d.id = e.idvApp_id
                                  where idCloud_id = """ + idCloud + """ and timestamp > '""" + str(hoy) + """'""" + filter + """  group by OSClean order by 1 """)
    #print(distros)
    
    ESX = kpisORG.objects.raw("""select * from reportinfra_esx where idCloud_id = """ + idCloud + """ order by ESX """)
    
    CPU = kpisORG.objects.raw("""
                              """)
    
    
    page_length = int(request.GET.get('length', 10))  # Número de registros por página
    start = int(request.GET.get('start', 0))  # Desde qué registro empezar
    #
    #
    #with connection.cursor() as cursor:
    #    # Consulta SQL
    #    cursor.execute("SELECT ORG, ORGvDC from reportinfra_kpisorg")  
    #    columns = [col[0] for col in cursor.description]  # Obtener nombres de columnas
    #    data = [dict(zip(columns, row)) for row in cursor.fetchall()]  # Convertir a diccionario
#
    #json_data = json.dumps(data, indent=4)
    
    #print(json_data)  # Ver JSON en consola
    
    #cursor.close()
    
    context = {
        "ESX" : ESX,
        "distros" : distros,
        "reporteORG" : reporteORG,
        "totalLinux" : totalLinux,
        "totalWin" : totalWin,
        "totalVM" : totalVM,
        "totalvPPA" : totalvPPA,
        "totalORG" : totalORG,
        "totalVDC" : totalVDC,
        "tag" : tagCloud,
        "cloud" : idCloud,
        "tag" : tagCloud,
    }

    return render(request, 'kpiCloud.html', context)

def detailORG(request):
    
    idCloud = request.GET.get("idCloud")    
    tagCloud = request.GET.get("id")
    
    
    if tagCloud == 'NET':
        filter = " and ORGvDC like concat(char(37), 'FLEX', char(37)) "
    else:
        filter = ""
    
    
    #qry = kpisORG.objects.raw("""select distinct 1 as id, a.ORG, c.vApp, Count(a.VM) VM, Sum(b.cpu) CPU, Sum(b.memoria) Memory, Sum(b.hdd) HDD
    #from reportinfra_kpisorg a
    #left join reportinfra_metadatavm b
    #on a.VM = b.VM and a.UUID = b.UUID
    #inner join vApp c
    #on a.ORG = c.ORG
    #where idCloud_id = """ + idCloud + filter +
    #""" group by a.ORG
    #order by 1""")
    
    #print(qry)
    
    context = {
     #   "qry" : qry,
    }
    
    return render(request, 'detailORG.html', context)

def obtener_datos_ajax(request):
    objetos = list(kpisORG.objects.values("id", "ORG", "ORGvDC"))
    return JsonResponse({"data": objetos})

def tabla_paginada(request):
    objetos = kpisORG.objects.all()
    paginator = Paginator(objetos, 10)  # 10 registros por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "test.html", {"page_obj": page_obj})