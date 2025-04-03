import bs4 as beautifulsoup
import requests
from requests import get
import pandas as pd
import pdfquery
import tkinter

#Procesar la página del BOE de las oposiciones como un PDF.

#lee el PDF como un objeto con PDFQUERY
pdf = pdfquery.PDFQuery("PDFs_BOE\BOE-A-2025-4761.pdf")
pdf.load() #carga PDF
"""
INTENTO, Buscar sintáxis del lenguaje
#mediante selectores tipo CSS, localizamos los elementos queridos

opo = BOE.pq("") 
#pq para localizar elementos, regresa un objeto PyQuery, representa los elementos seleccionados

#extrae la info
linea = []"
"""

#pasando el PDF a XML, solo nos tenemos que mover con un editor de texto, para ver donde están los datos que queremos extraer
pdf.tree.write("BOE-A-2025-4762.xml", pretty_print = True)
pdf

#Extraer información

puesto = pdf.pq('LTTextLineHorizontal:contains("PUESTO QUE SE SOLICITA")').text
print(puesto)
