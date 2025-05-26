import hashlib
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException
from monitor.models import BoletinURL, URLMonitor, FiltroGenerico  # Asegúrate de importar tu modelo de filtros

# Configurar logging
logging.basicConfig(level=logging.INFO)

def get_md5_of_text(text):
    return hashlib.md5(text.encode('utf-8')).hexdigest()
#Modificado por Samuel 21/05/2025 obtener palabras clave de la base de datos
def get_keywords_from_db():
    """
    Devuelve una lista de palabras clave de todos los filtros genéricos.
    """
    filtros = FiltroGenerico.objects.all()
    keywords = []
    for filtro in filtros:
        # Suponiendo que el campo 'palabras' contiene las palabras separadas por coma y espacio
        palabras = [p.strip().lower() for p in filtro.palabras.split(',')]
        keywords.extend(palabras)
    return keywords

def check_url_for_changes(url, old_hash, keywords):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    service = Service("chromedriver.exe")

    try:
        driver = webdriver.Chrome(service=service, options=chrome_options)
        try:
            chrome_options.add_argument("--ignore-certificate-errors")
            driver.get(url)
            full_text = driver.find_element(By.TAG_NAME, "body").text.strip()

            lower_text = full_text.lower()
            if not any(word in lower_text for word in keywords):
                return False, old_hash, None

            new_hash = get_md5_of_text(full_text)
            return (new_hash != old_hash), new_hash, full_text
        finally:
            driver.quit()
    except WebDriverException as e:
        logging.error(f"WebDriver error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

    return False, old_hash, None

def check_urls_from_models():
    """
    Lee las URLs de los modelos BoletinURL y URLMonitor, y verifica cambios usando los filtros de la base de datos.
    """
    urls = []

    # Obtener palabras clave de los filtros
    keywords = get_keywords_from_db()

    # Obtener URLs de BoletinURL
    boletin_urls = BoletinURL.objects.all()
    for boletin in boletin_urls:
        urls.append((boletin.url, boletin.hash))

    # Obtener URLs de URLMonitor
    url_monitor_urls = URLMonitor.objects.all()
    for monitor in url_monitor_urls:
        urls.append((monitor.url, monitor.hash))

    # Verificar cambios en cada URL
    for url, old_hash in urls:
        has_changed, new_hash, _ = check_url_for_changes(url, old_hash, keywords)
        if has_changed:
            logging.info(f"URL {url} ha cambiado.")
            # Actualizar el hash en la base de datos
            if BoletinURL.objects.filter(url=url).exists():
                BoletinURL.objects.filter(url=url).update(hash=new_hash)
            elif URLMonitor.objects.filter(url=url).exists():
                URLMonitor.objects.filter(url=url).update(hash=new_hash)