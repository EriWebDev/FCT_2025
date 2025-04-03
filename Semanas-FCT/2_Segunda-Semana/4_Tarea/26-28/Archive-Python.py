import requests
from bs4 import BeautifulSoup
from requests import get

#Ayuntamientos de Granada, Málaga y Salamanca
#Definir funciones
def get_data ():
    ayuntamientos = {
        "Granada" : "https://www.granada.org",
        "Malaga" : "https://www.malaga.eu",
        "Salamanca" : "https://www.aytosalamanca.es" 
    }
    """
    "ayuntamientos = {
        "Granada" : "https://www.granada.org",
        "Malaga" : "https://www.malaga.eu",
        "Salamanca" : "https://www.aytosalamanca.es" 
    }
    """

    def get_data_gr ():
        petition = requests.get(get_data["Granada"])
        if petition.status_code == 200:
            html_gr = petition.text
        else:
            print("Error al cargar la web del Ayuntamiento de Granada", petition.status_code)
        soup_gr = BeautifulSoup(html_gr, "html.parser")
        #tenemos que sacar alguna convocatoria para opositar, tb las coordenadas de 
