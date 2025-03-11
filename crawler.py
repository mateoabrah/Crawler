import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import csv

# Configurar el WebDriver y opciones de Chrome
chrome_driver_path = "chromedriver.exe"
service = Service(chrome_driver_path)
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(service=service, options=options)

# Función para obtener todos los enlaces internos de la página
def get_internal_links(url):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    soup = BeautifulSoup(driver.page_source, "html.parser")
    links = set()
    for link in soup.find_all("a", href=True):
        href = link["href"]
        full_url = urljoin(url, href)
        if urlparse(full_url).netloc == urlparse(url).netloc:  # Solo enlaces internos
            links.add(full_url)
    return links

# Función para verificar el código de estado HTTP
def check_http_status(url):
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.RequestException:
        return None  # Si ocurre algún error de conexión, devuelve None

# Función para explorar el dominio recursivamente
def crawl(url, visited, error_urls, max_links, link_count):
    if url not in visited and link_count < max_links:
        visited.add(url)
        link_count += 1
        print(f"Explorando: {url} - Enlaces revisados: {link_count}")
        links = get_internal_links(url)
        for link in links:
            status_code = check_http_status(link)
            if status_code and status_code >= 400 and status_code < 500:
                print(f"URL con error 4XX: {link} - {status_code}")
                error_urls.append([link, status_code, url])
            link_count = crawl(link, visited, error_urls, max_links, link_count)
    return link_count

# Iniciar el crawler
visited = set()
error_urls = []

# URL inicial
starting_url = "https://insbaixcamp.org/"
max_links = 100  # Limitar a 100 enlaces revisados
link_count = 0

link_count = crawl(starting_url, visited, error_urls, max_links, link_count)

# Guardar los resultados en un archivo CSV
if error_urls:
    with open("errores_4xx.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["URL con Error", "Código de Error", "Página de Origen"])
        writer.writerows(error_urls)
    print("Informe de errores guardado en errores_4xx.csv")
else:
    print("No se encontraron errores 4XX.")

# Cerrar el navegador
driver.quit()
