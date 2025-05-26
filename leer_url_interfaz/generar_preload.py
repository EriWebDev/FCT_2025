import pandas as pd

# Rutas a los archivos Excel
oposiciones_excel_path = "ServiciosSgtoConv2025.xlsx"
boletines_excel_path = "Lista _urls_de_boletines.xlsx"

# Hojas a procesar del archivo de oposiciones
hojas_oposiciones = ["Nacionales", "TBS", "PSV"]

#Nuevo codigo para que añada el http:// en las urls que no las tengan----------------------------- 
def normalizar_url(url):
    url = url.strip()
    if not url.startswith(("http://", "https://")):
        return "http://" + url
    return url
#este codigo se ha reemplazado 5/5/2025-----------------------

# Recoger URLs de todas las hojas de oposiciones
oposiciones_urls = []
for hoja in hojas_oposiciones:
    df = pd.read_excel(oposiciones_excel_path, sheet_name=hoja)
    if 'Enlace general sgto' in df.columns:
        urls = df['Enlace general sgto'].dropna().astype(str).str.strip().unique().tolist()
        oposiciones_urls.extend(urls)
    else:
        print(f"⚠️ La hoja '{hoja}' no contiene la columna 'Enlace general sgto'")

# Eliminar duplicados
oposiciones_urls = list(set(oposiciones_urls))

# Leer boletines
boletines_df = pd.read_excel(boletines_excel_path, sheet_name="boletines")
boletines_urls = boletines_df.iloc[:, 0].dropna().astype(str).str.strip().unique().tolist()

# Crear contenido para preload_urls.py
preload_content = '''from django.core.management.base import BaseCommand
from monitor.models import UrlMonitor, BoletinUrl

class Command(BaseCommand):
    help = "Carga inicial de URLs"

    def handle(self, *args, **kwargs):
        oposiciones_urls = [
'''

for url in oposiciones_urls:
    
    url = normalizar_url(url).replace("\n", "").replace("\r", "")
    safe_url = url.replace('"', '\\"')
    
    preload_content += f'            "{safe_url}",\n'

preload_content += '''        ]

        boletines_urls = [
'''

for url in boletines_urls:
    
    url = normalizar_url(url).replace("\n", "").replace("\r", "")
    safe_url = url.replace('"', '\\"')
     
    preload_content += f'            "{safe_url}",\n'

preload_content += '''        ]

        # Insertar URLs en UrlMonitor
        for url in oposiciones_urls:
            UrlMonitor.objects.get_or_create(url=url)

        # Insertar URLs en BoletinUrl
        for url in boletines_urls:
            BoletinUrl.objects.get_or_create(url=url)

        self.stdout.write(self.style.SUCCESS("URLs precargadas correctamente"))
'''

# Guardar el archivo
output_path = "monitor/management/commands/preload_urls.py"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(preload_content)

print(f"✅ preload_urls.py generado con {len(oposiciones_urls)} URLs de oposiciones y {len(boletines_urls)} URLs de boletines.")
