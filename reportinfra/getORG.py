import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
from time import sleep
from datetime import datetime
import mysql.connector
from termcolor import colored
import logging

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    filename='getORG.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def obtain_credentials(cloud, auth):
    URL_TOKEN = "https://" + cloud + "/api/sessions"
    credentials = {}    
    payload = {}

    headers = {        
        'Accept': 'application/*+json;version=36.0', # Change from xml to json
        'Authorization': 'Basic ' + auth
    }
    #print(headers)

    try:
        response = requests.post(URL_TOKEN, headers=headers, data=payload, verify=False)
        
        credentials['token'] = response.headers['X-VMWARE-VCLOUD-ACCESS-TOKEN']
        credentials['vcd_auth'] = response.headers['x-vcloud-authorization']
        print("Se obtiene el token: " + credentials['vcd_auth'])

    except Exception as error:
        print('Connection error: ' + str(error))
        exit()

    return credentials['token']

#def insertDB(ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, fechaAlta, totalUsr, idCloud):
def insertDB(sql, val, nube):
    try:
        
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="triara"
        )
        #ORG, fullName, fechaAlta, VDC, vAppOrg, vm_name, sistemaOpe, totalUsr, 3
        mycursor = mydb.cursor()

        #sql = """INSERT INTO reportinfra_kpisorg (ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
        #        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        #val = (ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, totalUsr, fechaAlta, datetime.now(), idCloud)

        mycursor.execute(sql, val)

        mydb.commit()
    
    except Exception as error:
        print("Error en la DB: " + str(error))
        logging.error("No se puede conectar a la DB, favor de validar: " + str(nube))
        #exit()
        
    finally:
        mydb.close()
        
def metaData(URL, token, orgID, ORG, fullname):

    headers = {
        'Accept' : 'application/*+json;version=36.0',
        'Authorization' : 'Bearer ' + token

    }
    #https://pubm-nube.telmex.com/api/admin/org/9d2df5a7-9f1b-450b-aa11-33d8707a1c12/metadata
    req = (requests.request("GET", "https://" + URL + "/api/admin/org/" + orgID + "/metadata", headers=headers, verify=False)).json()
    print("Obteniendo metadata ORG")
    #print(req)
    try:
        data1 = req["metadataEntry"][0]
        data2 = req["metadataEntry"][1]
        data3 = req["metadataEntry"][2]

        SAP = data1['typedValue']['value']
        TipoContratacion = data2['typedValue']['value']
        SA_Panel = data3['typedValue']['value']       

            

        sql = """INSERT INTO reportinfra_metadataorg (idORG, ORGname, SAP, TipoContratacion, SA_Panel) values (%s, %s, %s, %s, %s)"""
        val = (ORG, fullname, SAP, TipoContratacion, SA_Panel)
        #print("Valores de metadata: " + str(val))
        
        insertDB(sql, val, URL)
        

    except Exception as error:
        print(error)    

def metaVDC(URL, token, org):
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        'Authorization' : 'Bearer ' + token

    }
    
    #print("Obteniendo metadata OrgvDC")
    url = "https://" + URL + "/api/query?type=adminOrgVdc&filter=org==" + org
    #print(url)
    orgvdc = (requests.request("GET", url, headers=headers, verify=False)).json()
    
    try:
        
        for data in orgvdc["record"]:
            #print(data["href"])
            vdcName = data["name"]
            var = data["href"].split("/")
            vdc = var[6]

            req = (requests.request("GET", "https://" + URL + "/api/admin/vdc/" + vdc + "/metadata", headers=headers, verify=False)).json()
            print("Obteniendo metadata OrgVDC: " + str(vdcName))

            for data in req["metadataEntry"]:
                #print(str(data["key"]) + " - " + str(data["typedValue"]["value"]))
                c = data["key"]
                v = data["typedValue"]["value"]

                sql = """INSERT INTO reportinfra_metadataorgvdc (idORG, Campo, Valor) values (%s, %s, %s)"""
                val = (vdcName, c, v)

                insertDB(sql, val, URL)   
    except:
        print("No existe metadata para este vCD")
        
        
def metadataVM(URL, token, vm, ORG, nameVM):
    #print(token)
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        #'x-vcloud-authorization' : '979f4d213302445b9898750237677cdb'
        'Authorization' : 'Bearer ' + token
    }
    url = "https://" + URL + "/api/vApp/" + vm
    
    metaVM = (requests.request("GET", url, headers=headers, verify=False)).json()    
    print("Extrae metadata VM")
    
    print("Nombre: " + str(metaVM["name"]))
    print("CPU: " + str(metaVM["section"][0]["numCpus"]))
    print("Memory: " + str(metaVM["section"][0]["memoryResourceMb"]["configured"]))
    print("ESX: " + str(metaVM["vCloudExtension"][0]["any"][0]["hostVimObjectRef"]["moRef"]))
    print("Compute: " + str(metaVM["vdcComputePolicy"]["name"]))
    
    name = metaVM["name"]
    cpu = metaVM["section"][0]["numCpus"]
    memory = metaVM["section"][0]["memoryResourceMb"]["configured"]
    esx = metaVM["vCloudExtension"][0]["any"][0]["hostVimObjectRef"]["moRef"]
    policy = metaVM["vdcComputePolicy"]["name"]
    
    sql = """INSERT INTO reportinfra_metadatavm (idORG, cpu, host, memoria, VM, computePolicy) values (%s, %s, %s, %s, %s, %s)"""
    val = (ORG, cpu, esx, memory, name, policy)
    
    insertDB(sql, val, URL)

def processCloud(cloud, auth, idCloud): 
    cloud = cloud
    print(cloud)
    
    token = obtain_credentials(cloud, auth)
    #print(token)
    
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        'Authorization' : 'Bearer ' + str(token)

    }

    print("Se obtienen las ORG......")

    valorORG = "LUISGGGG"
    #Se obtienen las ORG
    req = (requests.request("GET", "https://" + cloud + "/api/org/",headers=headers, verify=False)).json()
    #print(req)
    for org in req["org"]:
        ORG = org["name"]
        
        urlORG = org["href"]
        uuid = urlORG.split("/")        
        vappOK = 0
        if ORG != valorORG:            
            try:
                print("ORG: " + ORG)
                #Se obtiene la fecha de registro de la ORG
                infoOrg = (requests.request("GET", urlORG, headers=headers, verify=False,timeout=60)).json()

                fullName = infoOrg['fullName'].replace(',','')
                x = "https://" + cloud + "/api/admin/org/" + uuid[5]
                #print("inserta metadatos: " + cloud + ' - ' + auth + ' - ' + uuid[5] + ' - ' + ORG + ' - ' + fullName)
                
                metaData(cloud, token, uuid[5], ORG, fullName)
                #print(x)
                metadata = x + "/metadata/SYSTEM/FECHA_ALTA"
                #print(metadata)
                
                metaVDC(cloud, token, uuid[5])

                fechaAlta = requests.get(metadata, headers=headers, verify=False,timeout=60)
                JsonFecha = fechaAlta.json()

                try:
                    fechaAlta = JsonFecha["typedValue"]["value"]
                    #print(fechaAlta)
                    #print("Fecha alta ORG: " + fechaAlta)
                except:
                    #print("No existe la entrada de fecha")
                    fechaAlta = datetime.now()
                    #print("Fecha alta alternativo ORG: " + str(fechaAlta))

                #Obtener el número de usuarios de la ORG
                urlUsers = "https://" + cloud + "/api/query?type=adminUser&filter=org==" + uuid[5]
                users = (requests.request("GET", urlUsers, headers=headers, verify=False,timeout=60)).json()
                totalUsr = users["total"]
                #print("Usuarios tenant: " + str(totalUsr))

                #obtener los ORGvDC
                detailVDC = (requests.request("GET", x, headers=headers, verify=False, timeout=60)).json()       
                suscription = detailVDC["description"]
                print(suscription)         
                #print(detailVDC)
                try:
                    print("Obtiene ORGvDC")
                    for vdc in detailVDC["vdcs"]["vdc"]:
                        urlVDC = vdc["href"]
                        VDC = vdc["name"]
                        #print("ORGvDC: " + VDC)

                        #obtener vApp por cada OrgVDC
                        vapps = (requests.request("GET", urlVDC, headers=headers, verify=False, timeout=60)).json()
                        print("Intentando obtener vAPPs")
                        for vapp in vapps["resourceEntities"]["resourceEntity"]:
                            urlvApp = vapp["href"]
                            vAppOrg = vapp["name"]
                            vappOK = 1
                            #print(urlvApp)
                            print("vApp: " + vAppOrg)

                            #obtener VMs de la vApp
                            VMs = (requests.request("GET", urlvApp, headers=headers, verify=False, timeout=60)).json()
                            print("Intentando obtener VM")
                            try:
                                for vm in VMs["children"]["vm"]:
                                    vm_name = vm["name"]
                                    #print("VM: " + vm_name)
                                    print("URL VM: " + vm["href"])
                                    vmUuid = vm["href"].split("/")
                                    
                                    metadataVM(cloud, token, vmUuid[5], ORG, vm_name)

                                    for os in vm["section"]:          
                                        if os["_type"] == "OperatingSystemSectionType":                                
                                            os = str(os['description']['value'])
                                            sistemaOpe = str(os)                                
                                            print(colored("Valores insertados: ", "green") + ORG + " - " + fullName + " - " + str(fechaAlta) + " - " + VDC + " - " 
                                            + vAppOrg + " - " + str(vm_name) + " - " + str(sistemaOpe) + " - " + str(totalUsr) + " - " + '3')

                                            sql = """INSERT INTO reportinfra_kpisorg (Suscripcion, ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
                                                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                                            val = (suscription, ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, totalUsr, fechaAlta, datetime.now(), idCloud)

                                            #insertDB(ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, fechaAlta, totalUsr, idCloud)
                                            insertDB(sql, val, cloud)     
                                            print("Primer insert")     
                                            print("")                              
                            except Exception as err:
                                print("No hay VM" + str(err)) 
                                print("")

                    if vappOK == 0:
                        print(colored("Valores insertados: ", "green") + ORG + " - " + fullName + " - " + str(fechaAlta) + " - " + VDC + " - " 
                        + "vAppOrg" + " - " + "str(vm_name)" + " - " + "str(sistemaOpe)" + " - " + str(totalUsr) + " - " + '3')
                        sql = """INSERT INTO reportinfra_kpisorg (Suscripcion, ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                        val = (suscription, ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, totalUsr, fechaAlta, datetime.now(), idCloud)
                        
                        insertDB(sql, val, cloud)
                        print("Segundo insert")
                        print("")
                            
                except:
                    print("La OrgVDC no tiene vApps ni VM")
                    
                    sql = """INSERT INTO reportinfra_kpisorg (Suscripcion, ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                    val = (suscription, ORG, "", fullName, "", "", "", "", "", datetime.now(), idCloud)                    
                    insertDB(sql, val, cloud)
                    print("Tercer insert")
                    print("")

                print(colored("*** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - *** - ***", "magenta"))

            except Exception as error:
                
                sql = """INSERT INTO reportinfra_kpisorg (Suscripcion, ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
                                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = ('123456789', ORG, "", fullName, "", "", "", "", "", datetime.now(), idCloud)
                
                print(colored("ERROR: No hay vCD que agregar", 'red'))
                insertDB(sql, val, cloud)
                print("Cuarto insert")
                print("")



def main():
    #AMX - bWFudWVsLm1lbmVzZXNAc3lzdGVtOlRyMTRyNEAyMDIx - 4
    #NPE - bW1lbmVzZXNAc3lzdGVtOk00bjM0QnJpbCNUM21wMHJhITIwMjQ= - 3
    #AMCO - b3N2V0ZzdmNAc3lzdGVtOms3MjZOQk16dVdtSzlYejFEMGhr - 2
    #NET 3 - b3N2LXZyb3BjbGQtc3ZjQHN5c3RlbTpMcFZfVHNya1A/ZTh3U2dXLmovNkJxXE1L - 7
    logging.info('Inicia el proceso de extracción')
    clouds = [
        {
            "cloud" : "NET 3",
            "vcloud": "prvq-nube.telmex.com",
            "key": "b3N2LXZyb3BjbGQtc3ZjQHN5c3RlbTpMcFZfVHNya1A/ZTh3U2dXLmovNkJxXE1L",
            "idCloud": "7",
        },
        {
            "cloud" : "AMX",
            "vcloud": "vcd.clarocloud.com",
            "key": "bWFudWVsLm1lbmVzZXNAc3lzdGVtOlRyMTRyNEAyMDIx",
            "idCloud": "1",
        },
        {
            "cloud" : "NPE",
            "vcloud": "pubm-nube.telmex.com",
            "key": "bW1lbmVzZXNAc3lzdGVtOkZGaTJsaGZPIXNaMjdHRipydHFe",
            "idCloud": "3",
        },
		{
            "cloud" : "AMCO",
            "vcloud": "ntcvvcd.telmex.com",
            "key": "b3N2V0ZzdmNAc3lzdGVtOms3MjZOQk16dVdtSzlYejFEMGhr",
            "idCloud": "2",
        }		
    ]

    y = json.dumps(clouds)

    for data in clouds:
        logging.info("Obteniendo datos de la nube: " + data["cloud"])
        print("Obteniendo datos de la nube: " + colored(data["cloud"], "cyan"))
        processCloud(data["vcloud"], data["key"], data["idCloud"])

logging.info("Termina el proceso")
main()

#metadataVM("prvq-nube.telmex.com", "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJhOTNjOWRiOS03NDcxLTMxOTItOGQwOS1hOGY3ZWVkYTg1ZjlAOGNmNTEzNzYtOWFjYi00MDIxLWJiZjMtYzM5NzZlYWFhNzQwIiwic3ViIjoib3N2LXZyb3BjbGQtc3ZjIiwiZXhwIjoxNzM5NDYyODcxLCJ2ZXJzaW9uIjoidmNsb3VkXzEuMCIsImp0aSI6Ijk3OWY0ZDIxMzMwMjQ0NWI5ODk4NzUwMjM3Njc3Y2RiIn0.YHEAiavOJW93g06x_YlzUmKT71K5iM54gdVHqJTIvrrcEucZMD5gKmdJIPGUPv5umzrKJXI0cOYviP7qHkEDXrGHMwKFd1Mh-KcrR8kMiJO1n9azwoOQXHcPDo1-YqDChcSfxtT-wUJiwtuQ-MUk_A3ooTLzZ7KqEHqc6AKA9YptEzPUCu9Tc3-IqD-Evmit9iHT3BaadwklzPgLSpNTHOPl5mH91UWft50rWwJRKkB61xBHPc9mOn4zU0h89o4_pQVTYN_zATrKCtF9un0e6AyFFyzofgul1EMmxJrgJarm4fOA35zcJA9D2Db1reJDwYiSF3vpBQrByvrrKhlaTw", "vm-1d702871-1d10-4b71-a9ad-92505348e117")

#metaVDC("prvq-nube.telmex.com", "b3N2LXZyb3BjbGQtc3ZjQHN5c3RlbTpMcFZfVHNya1A/ZTh3U2dXLmovNkJxXE1L", "ab1c0a58-b332-491c-901c-d1a2910c22e8")

#metadata('pubm-nube.telmex.com', 'bW1lbmVzZXNAc3lzdGVtOk00bjM0QnJpbCNUM21wMHJhITIwMjQ=', '3', '9d2df5a7-9f1b-450b-aa11-33d8707a1c12', '')

#obtain_credentials('ntcvvcd.telmex.com', 'b3N2V0ZzdmNAc3lzdGVtOms3MjZOQk16dVdtSzlYejFEMGhr')

#sql = """INSERT INTO reportinfra_kpisorg (ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#val = ('sadsa','ds','ds','dsad','dsadas','wqee','ewqewq','ewqe',datetime.now(),1)
#insertDB(sql, val)

#metadata('pubm-nube.telmex.com','bW1lbmVzZXNAc3lzdGVtOk00bjM0QnJpbCNUM21wMHJhITIwMjQ=', '9d2df5a7-9f1b-450b-aa11-33d8707a1c12', 'LUISG', 'Luis García CCC')