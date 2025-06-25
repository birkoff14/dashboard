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
    filename='getHW.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def obtain_credentials(cloud, auth):
    URL_TOKEN = "https://" + cloud + "/api/session"
    print(URL_TOKEN)
    credentials = {}    
    payload = {}

    headers = {        
        #'Accept': 'application/*+json;version=36.0', # Change from xml to json
        'Authorization': 'Basic ' + auth
    }
    #print(headers)

    try:
        response = requests.post(URL_TOKEN, headers=headers, data=payload, verify=False)
        
        credentials['token'] = response.headers['vmware-api-session-id']
        print("Se obtiene el token: " + credentials['token'])

        #print(response)

    except Exception as error:
        print('Connection error: ' + str(error))
        exit()

    return credentials['token']


def insertDB(sql, val, nube):
    try:
        
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="triara"
        )
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)

        mydb.commit()
    
    except Exception as error:
        print("Error en la DB: " + str(error))
        logging.error("No se puede conectar a la DB, favor de validar: " + str(nube))
        #exit()
        
    finally:
        mydb.close()


def getHW(token, URL, cloud):
    print("Tratando de obtener los HOST del vCenter")
    
    try:
        headers = {        
            'x-api-version' : '1.0-rev1',
            'Accept': 'application/json', 
            'vmware-api-session-id': token
        }

        req = (requests.request("GET", "https://" + URL + "/api/vcenter/host", headers=headers, verify=False)).json()

        for hosts in req:
            print(hosts["host"])
            print(hosts["name"])
            esx = hosts["host"]
            nameh = hosts["name"]
            
            sql = """INSERT INTO reportinfra_esx (idvCenter, ESX, Vendor, Host, idCloud_id) values (%s, %s, %s, %s, %s)"""
            val = (URL, nameh, "", esx, cloud)
    
            insertDB(sql, val, URL)
                   
    except Exception as err:
        print(err)

def getVM(token, URL, cloud):
    print("Tratando de obtener las VMs del vCenter")
    
    try:
        headers = {        
            'x-api-version' : '1.0-rev1',
            'Accept': 'application/json', 
            'vmware-api-session-id': token
        }

        req = (requests.request("GET", "https://" + URL + "/api/vcenter/vm", headers=headers, verify=False)).json()

        for hosts in req:
            print(hosts["vm"])
            print(hosts["name"])
            print(hosts["power_state"])
            vm = hosts["vm"]
            name = hosts["name"]
            state = hosts["power_state"]
            
            sql = """INSERT INTO reportinfra_vmesx (idvCenter, name, VM, State, idCloud_id) values (%s, %s, %s, %s, %s)"""
            val = (URL, name, vm, state, cloud)
    
            insertDB(sql, val, URL)
                   
    except Exception as err:
        print(err) 
        
def main():
    
    #URL = "mxap-npv-vcsr01.cloudmty.local"
    #auth = "YWRtaW5pc3RyYXRvckByZWN1cnNvcy5sb2NhbDpEdG10MiYxd3FRIXByZWZ5eGNAWg==222"
    #idCloud = 3
    
    #URL = "mxqrnet-paygo-vc-wld02.osvcloud.local"
    #auth = "bW1lbmVzZXNAb3N2Y2xvdWQ6XiQjNXV4MDZTRnVkMWlKISZHRlY="
    #idCloud = "7"
    
    URL = "172.30.168.10"
    auth = "bWFudWVsLm1lbmVzZXNAbnViZXRlbG1leC5sb2NhbDpEXjdWTVd2IUFAOTgyR2Q="
    idCloud = "2"
    
    token = obtain_credentials(URL, auth)
    
    getHW(token, URL, idCloud)
    getVM(token, URL, idCloud)

main()