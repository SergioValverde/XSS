#!/usr/bin/python

import requests
import colorama
from colorama import Fore

print (Fore.BLACK + "--------XSS-------")
print (Fore.BLUE + "Cargando modulos...")
print (Fore.BLACK + "-------------------")

# Fichero donde almacenamos los payloads
fname = "payloads.txt"

# Abrimos el fichero
with open(fname) as f:
    content = f.readlines()

# Recorremos el fichero y con la funcion strip eliminamos los espacios
payloads = [x.strip() for x in content] 

# Introducimos la url por pantalla
url = raw_input("Introduce una url: ")
print 
vuln = []

# Recorremos el fichero 
for payload in payloads:
    payload = payload

# Anadimos los payloads a nuestra url
    xss_url = url+payload

# Con la funcion requests.get, realizamos una solicitud get al target
    r = requests.get(xss_url)

# si el payload nos devuelve un contenido, es vulnerable
    if payload.lower() in r.text.lower():
        print(Fore.GREEN + "Vulnerable: " + payload)
	if(payload not in vuln):

# anade los payload en vuln
            vuln.append(payload) 
        else:
	        print (Fore.RED + "No es vulnerable!")



