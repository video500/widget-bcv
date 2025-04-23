from bs4 import BeautifulSoup
import requests

url="https://www.bcv.org.ve/"

response = requests.get(url, verify="bcv-org-ve-chain.pem")
soup = BeautifulSoup(response.text, "html.parser")

# Extraer información de un div con clase específica
dolar_div = soup.find("div", id="dolar")
if dolar_div:
    valor = dolar_div.find("div", class_="centrado").strong.text.strip()  # Extrae el texto dentro de <strong>
else:
    valor = "Error"
    
fecha_span = soup.find("span", class_="date-display-single")

if fecha_span:
    fecha_texto = fecha_span.text.strip()  # Extrae el texto visible (ej. Miércoles, 23 Abril 2025)
    fecha_iso = fecha_span["content"]  # Extrae la fecha en formato ISO (ej. 2025-04-23T00:00:00-04:00)
else:
    fecha_texto = "Error Fecha"
    
print (f"{fecha_texto}: {valor}")

