import requests #permite hacer peticiones HTTP para descargar archivos desde la web
from requests import get #obtener url
import re #regexp
import os #manejo archivos/directorios del SO (puede eliminar)
from pypdf import PdfReader #manipular archivos PDF
import threading #hilos

#"Varibles" - Datos
url_boe = ""
url_comunidades = [
    "Andalucia" = "", #BOJA - Boletín Oficial de la Junta de Andalucía
    "Madrid" = "",
    "Valencia" = "",
    "Salamanca" = ""
]


#Funciones
#1- Sacar pdf del BOE


#2- Sacar el pdf de una comunidad autónoma














if __name__ == "__main__":
    main()