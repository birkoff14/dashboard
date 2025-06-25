import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
from time import sleep
from datetime import datetime
import mysql.connector
from termcolor import colored
import logging
import uuid

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logging.basicConfig(
    filename='getORG.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def obtain_credentials(cloud, auth):
    if cloud == 'prvq-nube.telmex.com':
        URL_TOKEN = "https://" + cloud + "/cloudapi/1.0.0/sessions/provider"
        api = 39.1
    else:
        URL_TOKEN = "https://" + cloud + "/api/sessions"
        api = 36.0
    credentials = {}    
    payload = {}

    headers = {        
        'Accept': 'application/*+json;version=' + str(api), # Change from xml to json
        'Authorization': 'Basic ' + auth
    }
    #print(headers)

    try:
        response = requests.post(URL_TOKEN, headers=headers, data=payload, verify=False)
        
        credentials['token'] = response.headers['X-VMWARE-VCLOUD-ACCESS-TOKEN']
        credentials['vcd_auth'] = response.headers['X-VMWARE-VCLOUD-REQUEST-ID']
        print("Se obtiene el token: " + credentials['vcd_auth'])

    except Exception as error:
        print('Connection error: ' + str(error))
        exit()

    return credentials['token']

#def insertDB(ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, fechaAlta, totalUsr, idCloud):
def insertDB(sql, val):
    try:
        last_id = 0
        
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Django2025",
            database="triara"
        )
        #ORG, fullName, fechaAlta, VDC, vAppOrg, vm_name, sistemaOpe, totalUsr, 3
        mycursor = mydb.cursor()

        #sql = """INSERT INTO reportinfra_kpisorg (ORG, ORGvDC, NombreORG, vApp, VM, OS, NoUsuarios, FechaAlta, timestamp, idCloud_id) 
        #        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        #val = (ORG, VDC, fullName, vAppOrg, vm_name, sistemaOpe, totalUsr, fechaAlta, datetime.now(), idCloud)

        mycursor.execute(sql, val)
        last_id = mycursor.lastrowid

        mydb.commit()
    
    except Exception as error:
        print("Error en la DB: " + str(error))
        #logging.error("No se puede conectar a la DB, favor de validar: " + str(nube))
        #exit()
        
    finally:
        mydb.close()
        return last_id
        
def getORGvDC(token, cloud, uuid, last):
    
    URL = "https://" + cloud + "/api/admin/org/" + uuid
    
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        'Authorization' : 'Bearer ' + str(token)
    }
    detailVDC = (requests.request("GET", URL, headers=headers, verify=False, timeout=60)).json()
    suscription = detailVDC["description"]
    #print(suscription)
    try:
        for vdc in detailVDC["vdcs"]["vdc"]:
            urlVDC = vdc["href"]
            uuidORG = urlVDC.split("/")        
            myuuid = uuidORG[6].replace("-","") 
            orgVDC = vdc["name"]
            #print(orgVDC)
            
            sql = """INSERT INTO reportinfra_kpiorgvdcv2 (UUID_id, idVDC, ORGvDC)
                  VALUES (%s, %s, %s)"""
            val = (last, myuuid, orgVDC)

            last_id = insertDB(sql, val)
            
            getvApp(urlVDC, token, last_id)
            
    except Exception as err:
        print(err)
        
def getvApp(url, token, last_id):
    
    print("Obteniendo vAPPs")
    
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        'Authorization' : 'Bearer ' + str(token)
    }
    
    try:
        vapps = (requests.request("GET", url, headers=headers, verify=False, timeout=60)).json()
        if vapps["resourceEntities"]["resourceEntity"] is None:
            print("NO existen vAPPS, se agregará solamente la ORG")
        else:
            for vapp in vapps["resourceEntities"]["resourceEntity"]:
                if vapp["type"] == "application/vnd.vmware.vcloud.vApp+xml":
                    print("Es vAPP válida")
                    urlvApp = vapp["href"]
                    vAppOrg = vapp["name"]                            
                    #print(urlvApp)
                    #print("vApp: " + vAppOrg)
                    #revisa que no sea una vAPP de sistema

                    sql = """INSERT INTO reportinfra_kpivappv2 (idvApp, vApp, idVDC_id)
                      VALUES (%s, %s, %s)"""
                    val = ('', vAppOrg, last_id)

                    last_vapp = insertDB(sql, val)       
                    #print("last_vapp: " + str(last_vapp))

                    VMs = (requests.request("GET", urlvApp, headers=headers, verify=False, timeout=60)).json()      
                    print("Obteniendo VMs")
                    try:
                        if VMs["children"]["vm"] is None:
                            print("No existen VM en esta vAPP")
                        else:
                            for vm in VMs["children"]["vm"]:
                                vm_name = vm["name"]
                                #print("VM: " + vm_name)
                                #print("URL VM: " + vm["href"])
                                vmUuid = vm["href"].split("/")
                                for os in vm["section"]:          
                                    if os["_type"] == "OperatingSystemSectionType":                                
                                        os = str(os['description']['value'])
                                        sistemaOpe = str(os)
                                        #print(sistemaOpe)

                                        sql = """INSERT INTO reportinfra_kpivmv2 (idVM, VM, OS, UUIDVM, idvApp_id)
                                              VALUES (%s, %s, %s, %s, %s)"""
                                        val = ('', vm_name, sistemaOpe, '', last_vapp)

                                        last_vm = insertDB(sql, val)

                            metadataVM(vm["href"], token, last_vm)

                    except Exception as err:
                        print(err)                       
            
    except Exception as err:
        print(err)
        
        
def metadataVM(URL, token, last_vm):
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        #'x-vcloud-authorization' : '979f4d213302445b9898750237677cdb'
        'Authorization' : 'Bearer ' + token
    }
    
    #print(URL)
    
    metaVM = (requests.request("GET", URL, headers=headers, verify=False)).json() 
    print("Extrae metadata VM")
    
    name = metaVM["name"]
    print(name)
    cpu = metaVM["section"][0]["numCpus"]
    memory = metaVM["section"][0]["memoryResourceMb"]["configured"]
    esx = metaVM["vCloudExtension"][0]["any"][0]["hostVimObjectRef"]["moRef"]
    policy = metaVM["vdcComputePolicy"]["name"]
    IDVM = metaVM["vCloudExtension"][0]["any"][0]["vmVimObjectRef"]["moRef"]
    
    try:
        allDisk=0
        for info in metaVM['section']:
            for disk in info['diskSection']['diskSettings']:
                allDisk+=int(disk['sizeMb'])
                #print("Tamaño disco: " + str(allDisk/1024))
                
                sql = """INSERT INTO reportinfra_kpimetadatavmv2 (VM, cpu, memoria, host, computePolicy, idVM, hdd, UUID, idvApp_id)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                val = (name, cpu, memory, esx, policy, IDVM, allDisk, '', last_vm)

                insertDB(sql, val)
                
    except Exception as err:
        print("Error Disco: " + str(err))    
    
        

def processCloud(cloud, auth, idCloud):
    token = obtain_credentials(cloud, auth)    
    
    headers = {
        'Accept' : 'application/*+json;version=36.0',
        'Authorization' : 'Bearer ' + str(token)
    }
    
    print("Se obtienen las ORG......")
     
    valorORG = "LUISGxxxxx" #COCULA  ABASTECEDORA AMXMOVIL
    tORG = 0
    req = (requests.request("GET", "https://" + cloud + "/api/org/",headers=headers, verify=False)).json()
    for org in req["org"]:
        ORG = org["name"]
        urlORG = org["href"]
        uuidORG = urlORG.split("/")        
        myuuid = uuidORG[5].replace("-","")        
        if ORG != valorORG: #<-- AQUI SE CAMBIA LA ORG A FILTRAR
            #print(ORG)
            #logging.info(ORG)
            infoOrg = (requests.request("GET", urlORG, headers=headers, verify=False,timeout=60)).json()        
            fullName = infoOrg['fullName'].replace(',','')
            desc = infoOrg['description']
            #logging.info(fullName + " " + desc)
            
            x = "https://" + cloud + "/api/admin/org/" + uuidORG[5]
            
            fechAltaORG = x + "/metadata/SYSTEM/FECHA_ALTA"
            
            fechaAlta = requests.get(fechAltaORG, headers=headers, verify=False,timeout=60)            
            JsonFecha = fechaAlta.json()
            
            try:
                fechaAlta = JsonFecha["typedValue"]["value"]
            except:
                fechaAlta = datetime.now()         
            
            urlUsers = "https://" + cloud + "/api/query?type=adminUser&filter=org==" + uuidORG[5]
            users = (requests.request("GET", urlUsers, headers=headers, verify=False,timeout=60)).json()
            totalUsr = users["total"]
            
            #logging.info(ORG)
            
            sql = """INSERT INTO reportinfra_kpiorgv2 (Suscripcion, ORG, NombreORG, NoUsuarios, FechaAlta, timestamp, idCloud_id, UUID) 
                                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            val = (desc, ORG, fullName, totalUsr, fechaAlta, datetime.now(), idCloud, myuuid)
            
            last_id = insertDB(sql, val)
            tORG += 1
            
            #Orgvdc
            getORGvDC(token, cloud, uuidORG[5], last_id)
            #Metadata ORG
            #Metadata OrgvDC
            #MetadataVM
            
    #print("Se encontraron un total de: " + str(tORG)) + " organizaciones" 
    
    
    
        
#processCloud('pubm-nube.telmex.com', 'bW1lbmVzZXNAc3lzdGVtOjVaYjFsd3RQOEBVU3lJNmNAS0Ek','3')


def main():
    logging.info(str(datetime.now()) + ' Inicia el proceso de extracción')
    print(str(datetime.now()) + " - Inicia proceso")
    
    cloudsxxx = [
        {
            "cloud" : "NET 3",
            "vcloud": "prvq-nube.telmex.com",
            "key": "b3N2LXZyb3BjbGQtc3ZjQHN5c3RlbTorQlxQO3EhWCErejdQLGthLUoubHdtZWpx",
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
            "key": "bW1lbmVzZXNAc3lzdGVtOjVaYjFsd3RQOEBVU3lJNmNAS0Ek",
            "idCloud": "3",
        },
		{
            "cloud" : "AMCO",
            "vcloud": "ntcvvcd.telmex.com",
            "key": "b3N2V0ZzdmNAc3lzdGVtOms3MjZOQk16dVdtSzlYejFEMGhr",
            "idCloud": "2",
        }		
    ]
    
    clouds = [
        {
            "cloud" : "NET 3",
            "vcloud": "prvq-nube.telmex.com",
            "key": "b3N2LXZyb3BjbGQtc3ZjQHN5c3RlbTorQlxQO3EhWCErejdQLGthLUoubHdtZWpx",
            "idCloud": "7",
        }
    ]

    for data in clouds:
        logging.info("Obteniendo datos de la nube: " + data["cloud"])
        print(str(datetime.now()) + " Obteniendo datos de la nube: " + colored(data["cloud"], "cyan"))
        processCloud(data["vcloud"], data["key"], data["idCloud"])
    
    
    print(str(datetime.now()) + " - Termina proceso")
    logging.info(str(datetime.now()) + 'Termina el proceso de extracción')
    
main()
#processCloud("ntcvvcd.telmex.com", "b3N2V0ZzdmNAc3lzdGVtOms3MjZOQk16dVdtSzlYejFEMGhr", "2")
#obtain_credentials('ntcvvcd.telmex.com', 'b3N2V0ZzdmNAc3lzdGVtOms3MjZOQk16dVdtSzlYejFEMGhr')