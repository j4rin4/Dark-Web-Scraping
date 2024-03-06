#VENDETA V2
import requests, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from format_results import format_results
from settings import get_desktop_directory, setup_directory

# Establecimiento del path del escritorio y configuración inicial del directorio
desktop_path = get_desktop_directory()

setup_directory()

def Vendetta():
     # URL base del sitio a scrapear
    base_url = "http://test.cuba4ikm4jakjgmkezytyawtdgr2xymvy6nvzgw5cglswg3si76icnqd.onion"
     # Inicialización de estructura para almacenar datos extraídos
    publications = {"nom": [], "data": [], "pagina": [], "captura": []}

    # Configuración de la sesión de requests con proxy para acceder a la red Tor
    session = requests.session()
    session.proxies["http"] = "socks5h://localhost:9050"
    session.proxies["https"] = "socks5h://localhost:9050"

    chrome_options = ChromeOptions()
    chrome_options.add_argument("--proxy-server=socks5://localhost:9050")
    # Inicialización del navegador Chrome con Selenium
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        response = session.get(base_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        publication_links = [base_url + link["href"] for link in soup.find_all("a", class_="btn btn-post")]

        for publicacion_link in publication_links:
            try:
                response = session.get(publicacion_link)
                response.raise_for_status()
                publicacion_soup = BeautifulSoup(response.content, "html.parser")

                # Extracción de datos con BeautifulSoup
                nombre_element = publicacion_soup.find("h2")
                nombre = nombre_element.text.strip() if nombre_element else "Nombre no encontrado"
                # Agregar aquí la lógica para extraer la fecha y otros datos necesarios

                # Navegación con Selenium para captura de pantalla
                driver.get(publicacion_link)
                screenshot_filename = os.path.basename(publicacion_link) + ".png"
                screenshot_path = f"/home/j4rin4/Escritorio/MEDIA/Vendetta/{screenshot_filename}"
                driver.save_screenshot(screenshot_path)

                publications["nom"].append(nombre)
                publications["data"].append("Fecha extraída")  # Modificar según la lógica de extracción de fecha
                publications["pagina"].append(publicacion_link)
                publications["captura"].append(screenshot_path)

            except Exception as e:
                print(f"Error al procesar {publicacion_link}: {e}")

    except Exception as e:
        print(f"Error al acceder a {base_url}: {e}")

    finally:
        driver.quit()

    formatted_results = format_results(publications)
    return formatted_results

if __name__ == "__main__":
    resultados = Vendetta()
    print(resultados)

#By j4rin4