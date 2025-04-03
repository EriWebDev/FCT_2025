import bs4 as beautifulsoup
import requests #permite hacer peticiones HTTP para descargar archivos desde la web
from requests import get #obtener url
import re #regexp
import os #manejo archivos/directorios del SO (puede eliminar)
import pandas as pd #procesar y analizar
from pypdf import PdfReader #manipular archivos PDF
import threading #hilos

#si se importa el código desde otro módulo, __name__ se establecerá en el nombre de ese módulo
#__name__ para el archivo que se ejecute siempre será __main__. Pero para todos los demás que se importan mostrará el nombre de su módulo
if __name__ == "__main__":
    (f"Nombre de boe_PyPDF: {__name__}")

#función para extraer la url del BOE y buscar la info
#Todas las acciones para sacar URL y PDF
def pag_boe (url):
    boe = requests.get(url) #descarga PDF desde la URL. Hace petición HTTP y obtiene el contenido del archivo PDF
        
    # if boe.status_code != 200:
    #     print("Error", boe.status_code)
    #     return
    # try:
    #     response = requests.get(url)
    #     response.raise_for_status()  # Lanza una excepción si el código de estado no es 200}
    #except rquests.exceptions.RequestException as 

    #ESCRIBIR. PARA descargar y crear pdf. Se guarda el contenido descargado en un archivo
    with open("../PDFs_BOE/BOE-A-2025-4761.pdf", "wb") as a: #se guarda el contenido en el archivo en modo binario (wb)
        a.write(boe.content)
    
    #LECTURA. PARA leer el archivo
    with open("../PDFs_BOE/BOE-A-2025-4761.pdf", "rb") as b: #lectura binaria (rb)
        read_pdf = PdfReader(b) #PdfReader para poder leer su contenido
        content = "" #se guarda el texto del PDF en una variable
        
        #LECTURA. con el bucle for, recorremos cada página del PDF y extraemos el texto, guardándolo en a variable anteriormente inicializada
        for page in read_pdf.pages: #por cada página, en la variable donde se lee el contenido, conjunto como páginas
            text = page.extract_text()
            if text:
                content += text #se le suma cada página a contenido
        
        #RegExp para buscar palabras en el texto
        opos = re.findall(r"\b(Denominación del puesto)\b", content, re.IGNORECASE) # re.findall()-> RegExp para buscar la palabra en el content. re.IGNORECASE-> no distinguir mayus de minus  
    
    #sacamos por consola el contenido para visualizarlo
    print(f"Del enlace {url} : {opos}") # casi igual a: print("Del enlace", url, ": ", opos)
#la f ("formatted string literals") anterior es para que en lugar de imprimir {url}, imprima lo que se ha guardado dentro de esa variable
    
    #seguimos dentro de la función, ahora eleminar el pdf, para lo que usamos os
    if os.path.exists("PDFs_BOE/BOE-A-2025-4761.pdf"):
        os.remove("PDFs_BOE/BOE-A-2025-4761.pdf") #remove


#otra función para extraer la url de las opos de las comunidades y buscar la info
def pag_comun(urls): #url en plural al ser 17 comunidades y 2 ciudades autónomas
    #bucle for para recorrear cara Url de una lista
    for url in urls:
        ans = requests.get(url)

        # if ans.status_code == 200:
        #     url == ans.text
        # else:
        #     print("Error", ans.status_code)

        #ESCRIBIR. Igual que en la primera función. Guardar contenido PDF en wb, binario
        with open("../PDFs_comunidades/AnuncioG0767-250325-0006_gl.pdf", "wb") as c: #se guarda el contenido en el archivo en modo binario (wb)
            c.write(ans.content) #guardamos la respuesta de la URL
    
        #LECTURA. PARA leer el archivo
        with open("../PDFs_comunidades/AnuncioG0767-250325-0006_gl.pdf", "rb") as d: #lectura binaria (rb)
            read_pdf = PdfReader(d) #PdfReader para poder leer su contenido
            content = "" #se guarda el texto del PDF en una variable
        
        #LECTURA. con el bucle for, recorremos cada página del PDF y extraemos el texto, guardándolo en a variable anteriormente inicializada
        for page in read_pdf.pages: #por cada página, en la variable donde se lee el contenido, conjunto como páginas
            content += page.extract_text() #se le suma cada página a contenido
        
        #RegExp para buscar palabras en el texto
        opos = re.findall(r"\b(Oposiciones|oposición)\b", content, re.IGNORECASE) # re.findall()-> RegExp para buscar la palabra en el content. re.IGNORECASE-> no distinguir mayus de minus  
    
        #sacamos por consola el contenido para visualizarlo
        print(f"Del enlace {url} : {opos}")

        #dentro de la función, eliminar pdf
        if os.path.exists("../PDFs_comunidades/AnuncioG0767-250325-0006_gl.pdf"):
            os.remove("PDFs_comunidades/AnuncioG0767-250325-0006_gl.pdf") 

#Contenidos
#URL BOE
url_Boe = "https://www.boe.es/boe/dias/2025/03/11/pdfs/BOE-A-2025-4761.pdf"
#Lista urls para las comunidades
urls_comun = [
    'https://www.xunta.gal/dog/Publicados/2025/20250331/AnuncioG0767-250325-0006_gl.pdf',
    'https://www.juntadeandalucia.es/eboja/2025/47/BOJA25-047-00213-3298-01_00316903.pdf'    
]

#Hilos
#funciones
#creamos un hilo para ejecutar cada función
thread_opos = threading.Thread(target=pag_boe, args=(url_Boe,)) #la coma al final del contenido de args, es para pasar un solo argumento, sino se tomaría como una tupla sin elementos en Python
thread_comun = threading.Thread(target=pag_comun, args=(urls_comun,))

#inicialización de los hilos
thread_opos.start()
thread_comun.start()

#esperar a que terminen los hilos
thread_opos.join() #.join hace que el programa espere a que los hilos terminen antes de continuar
thread_comun.join()



"""
Resumen por pasos:
1. Crear funciones, "acciones" a realizar
2. Se añaden las variables, la "info" que va a realizar esas "acciones"
3.Creación de los hilos
4. Inicialización de los hilos con .join
"""

"""
Anotaciones extra:
- Cuidar la sintaxis, repasar lo escrito, a veces escribes mal
- Python usa / en vez de \
- A la hora de crear los hilos, target=tatata, va todo seguido, junto
- Creación de hilos: args=tata, -> Tiene que terminar en coma, para que tome un elemento
- Se te olvicó iniciar los hilos
- Investiga try-except para tratar status_code

"""