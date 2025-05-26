import subprocess
import webbrowser
import time
import os
import sys


# Establecer variable de entorno para Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "url_monitor.settings")

import os
import sys

# Obtener la ruta del ejecutable o script
exe_path = os.path.dirname(os.path.abspath(sys.argv[0]))

# Subir un nivel desde el ejecutable (estás en dist/)
BASE_DIR = os.path.abspath(os.path.join(exe_path, '..'))

# Cambiar al directorio raíz del proyecto Django
os.chdir(BASE_DIR)


# Aplicar migraciones
subprocess.call(["python", "manage.py", "migrate"])

# Esperar unos segundos antes de abrir el navegador
def open_browser_later():
    time.sleep(2)  # Esperar 2 segundos
    webbrowser.open("http://127.0.0.1:8000/")

# Iniciar apertura del navegador en un hilo paralelo
import threading
threading.Thread(target=open_browser_later).start()

# Ejecutar el servidor Django
subprocess.call(["python", "manage.py", "runserver"])
